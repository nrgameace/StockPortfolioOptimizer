from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <--- NEW LINE
from pydantic import BaseModel
from src.next_day_weights import next_day_weights

app = FastAPI()

# Allowed servers
origins = [
    # Local development
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    # CloudFront URL
    "https://d2h8y2m1123u28.cloudfront.net/",

    "https://s3fathmwjw.us-east-1.awsapprunner.com/"
]

# 2. ADD THE MIDDLEWARE TO THE APP
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # List of origins that are allowed to make requests
    allow_credentials=True,         # Allows cookies/authorization headers to be included
    allow_methods=["*"],            # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],            # Allows all headers
)

# Create a class using Pydantic to standardize data sent
class StockBudgetInput(BaseModel):
    tickers: list
    initial_value: float 
    weights: list
    expected_return: float
    expected_variance: float


@app.post("/submit-portfolio")
async def process_stock_and_budget_data(data: StockBudgetInput):
    
    # Grab initial data being sent in
    tickers_received = data.tickers
    initial_value_received = data.initial_value
    print("Recieved data")


    weights, expected_return, expected_variance = next_day_weights(tickers_received, initial_value_received)

    # POST returns JSON format
    return {
        "status": "done",
        "tickers": tickers_received,
        "initial_value": initial_value_received,
        "weights": weights.tolist(),
        "expected_return": expected_return,
        "expected_variance": expected_variance,
        
    }

@app.get("/")
async def root():
    return {"status": "ok"}