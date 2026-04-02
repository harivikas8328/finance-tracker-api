from pydantic import BaseModel
from datetime import date

class TransactionBase(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: str | None = None

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int

    class Config:
        from_attributes = True
