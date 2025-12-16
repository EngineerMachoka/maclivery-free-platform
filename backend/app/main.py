# backend/app/main.py
# This is the main entry point for the FastAPI application

# Import FastAPI framework
from fastapi import FastAPI

# Import database initialization function
from app.db import init_db

# Import order creation logic
from app.orders import create_order

# Create FastAPI app instance
app = FastAPI(
    title="Maclivery Free Platform API",
    description="Demonstration marketplace for Kenya & UK operations",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    """
    Runs automatically when the API starts.
    Ensures all database tables exist.
    """
    init_db()

@app.post("/orders")
def place_order(
    buyer_id: int,
    seller_id: int,
    amount_cents: int,
    currency: str
):
    """
    REST endpoint to create a paid order.
    """
    return create_order(
        buyer_id=buyer_id,
        seller_id=seller_id,
        amount_cents=amount_cents,
        currency=currency
    )

@app.get("/")
def root():
    """
    Health check endpoint.
    Used to confirm API is running.
    """
    return {"status": "Maclivery API running"}
