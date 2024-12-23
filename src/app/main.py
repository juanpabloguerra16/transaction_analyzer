from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.app.repository import DataRepository, Transaction

app = FastAPI()
data_repository = DataRepository()

@app.post("/analyze-transactions")
async def analyze_transactions(transactions: List[Transaction]):
    try:
        result = data_repository.process_transactions(transactions)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
