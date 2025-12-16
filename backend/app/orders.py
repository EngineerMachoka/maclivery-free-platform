# backend/app/orders.py
# This file handles order creation logic

# Import Order model
from app.models import Order

# Import database session helper
from app.db import get_session

# Import fee calculation logic
from app.fees import calculate_fees

def create_order(buyer_id: int, seller_id: int, amount_cents: int, currency: str):
    """
    Creates a new order in the system.

    IMPORTANT RULE:
    - Orders are only created if payment is successful.
    - In the FREE VERSION, payment success is simulated.
    """

    # Calculate all platform fees
    fees = calculate_fees(amount_cents)

    # Open database session
    with get_session() as db:

        # Create a new Order record
        order = Order(
            buyer_id=buyer_id,        # Who is buying
            seller_id=seller_id,      # Who is selling
            amount_cents=amount_cents,
            currency=currency,
            paid=True                 # Payment enforced here
        )

        # Save order to database
        db.add(order)
        db.commit()

        # Refresh object to get generated ID
        db.refresh(order)

    # Return order details and fee breakdown
    return {
        "order_id": order.id,
        "amount_cents": amount_cents,
        "currency": currency,
        "fees": fees
    }
