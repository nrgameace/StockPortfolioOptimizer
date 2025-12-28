from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.next_day_weights import next_day_weights
import logging
import sys
import os

# Configure logging to output to stdout (required for App Runner)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ],
    force=True
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Allowed servers
origins = [
    # Local development
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    # CloudFront URL
    "https://d2h8y2m1123u28.cloudfront.net",
    # App Runner URL
    "http://35.172.69.226:8000",
    "http://35.172.69.226:443",
    "http://35.172.69.226:80",
    "https://portfoliooptimizer.nickolasregas.com",

]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a class using Pydantic to standardize data sent
class StockBudgetInput(BaseModel):
    tickers: list
    initial_value: float 
    weights: list
    expected_return: float
    expected_variance: float


@app.on_event("startup")
async def startup_event():
    """Log important info when the app starts"""
    logger.info("App started successfully")


@app.get("/")
async def root():
    """Root endpoint - basic health check"""
    return {"status": "ok", "service": "stock-portfolio-optimizer"}


@app.get("/health")
async def health_check():
    """Lightweight health check endpoint for App Runner"""
    return {"status": "healthy"}


@app.post("/submit-portfolio")
async def process_stock_and_budget_data(data: StockBudgetInput):
    """Process portfolio data and return optimized weights"""
    try:
        tickers_received = data.tickers
        initial_value_received = data.initial_value
        
        # Calculate optimized weights
        weights, expected_return, expected_variance = next_day_weights(
            tickers_received, 
            initial_value_received
        )
        
        # POST returns JSON format
        return {
            "status": "done",
            "tickers": tickers_received,
            "initial_value": initial_value_received,
            "weights": weights.tolist(),
            "expected_return": expected_return,
            "expected_variance": expected_variance,
        }
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        
        # Return error response
        return {
            "status": "error",
            "message": str(e)
        }


# Log when module is imported
logger.info("api.py module loaded successfully")
