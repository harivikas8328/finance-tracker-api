from fastapi import FastAPI
from database import engine, Base
from routes import transactions, summary

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Tracker API")

app.include_router(transactions.router)
app.include_router(summary.router)
@app.get("/")
def home():
    return {"message": "Finance API is running 🚀"}