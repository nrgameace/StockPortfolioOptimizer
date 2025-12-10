from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <--- NEW LINE
from pydantic import BaseModel
from src.next_day_weights import next_day_weights

app = FastAPI()

# ----------------------------------------------------
# 1. DEFINE ALLOWED ORIGINS (The domains/ports allowed to access your API)
# Since you are running locally, use the origins below.
origins = [
    # Allows requests from the localhost on the default port 8000 (if you have two APIs)
    "http://localhost:8000",
    # Allows requests from any origin (e.g., file:// or any other local port) - USE WITH CAUTION IN PRODUCTION!
    "http://127.0.0.1:8000",
    "*" # Allows ALL origins. Easiest for local development but unsafe for production.
]

# 2. ADD THE MIDDLEWARE TO THE APP
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # List of origins that are allowed to make requests
    allow_credentials=True,         # Allows cookies/authorization headers to be included
    allow_methods=["*"],            # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],            # Allows all headers
)

class StockBudgetInput(BaseModel):
    tickers: str
    initial_value: float 

@app.post("/submit-portfolio")
async def process_stock_and_budget_data(data: StockBudgetInput):
    
    tickers_received = data.tickers
    initial_value_received = data.initial_value
    print("Recieved data")
    print(tickers_received)
    tickers_received = tickers_received.split(',')
    weights = next_day_weights(tickers_received, initial_value_received)
    return {
        "status": "done",
        "tickers": tickers_received,
        "initial_value": initial_value_received,
        "weights": weights,
    }