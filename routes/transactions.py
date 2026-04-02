from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas
from utils.role_checker import require_role

router = APIRouter(prefix="/transactions", tags=["Transactions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from utils.role_checker import require_role

@router.post("/", response_model=schemas.TransactionResponse)
def create_transaction(
    data: schemas.TransactionCreate,
    db: Session = Depends(get_db),
    role_check: str = Depends(require_role("admin"))
):
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    if data.type not in ["income", "expense"]:
        raise HTTPException(status_code=400, detail="Invalid type")

    txn = models.Transaction(**data.model_dump())
    db.add(txn)
    db.commit()
    db.refresh(txn)
    return txn

@router.get("/")
def get_transactions(db: Session = Depends(get_db), type: str = None, category: str = None):
    query = db.query(models.Transaction)

    if type:
        query = query.filter(models.Transaction.type == type)
    if category:
        query = query.filter(models.Transaction.category == category)

    return query.all()


@router.put("/{txn_id}")
def update_transaction(txn_id: int, data: schemas.TransactionCreate, db: Session = Depends(get_db)):
    txn = db.query(models.Transaction).filter(models.Transaction.id == txn_id).first()
    
    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    
    for key, value in data.model_dump().items():
        setattr(txn, key, value)

    db.commit()
    db.refresh(txn)   
    return txn
@router.delete("/{txn_id}")
def delete_transaction(txn_id: int, db: Session = Depends(get_db)):
    txn = db.query(models.Transaction).filter(models.Transaction.id == txn_id).first()
    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(txn)
    db.commit()
    return {"message": "Deleted successfully"}
