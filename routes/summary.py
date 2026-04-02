from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from sqlalchemy import func

router = APIRouter(prefix="/summary", tags=["Summary"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/totals")
def get_totals(db: Session = Depends(get_db)):
    income = db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type == "income").scalar() or 0
    expense = db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type == "expense").scalar() or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }

@router.get("/category")
def category_breakdown(db: Session = Depends(get_db)):
    result = db.query(models.Transaction.category, func.sum(models.Transaction.amount)).group_by(models.Transaction.category).all()

    return [{"category": r[0], "total": r[1]} for r in result]
