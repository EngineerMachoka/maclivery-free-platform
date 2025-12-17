# backend/app/orders.py
# Handles order creation with Tide UK enforcement

from app.models import Order
from app.db import get_session
from app.fees import calculate_fees
from app.payments_tide import process_tide_payment

def create_order(buyer_id: int, seller_id: int, amount_cents: int, currency: str, buyer_country: str):
    """
    Creates an order with strict payment enforcement.

    RULES:
    - UK users MUST pay via Tide
    - Orders cannot exist without confirmed payment
    """

    # If buyer is from UK, enforce Tide payment
    if buyer_country == "UK":

        # Attempt Tide payment
        payment_result = process_tide_payment(buyer_id, amount_cents)

        # If Tide payment fails, reject order
        if not payment_result["success"]:
            return {
                "error": "Tide payment failed. Order not created."
            }

    # Calculate platform fees
    fees = calculate_fees(amount_cents)

    # Save order only AFTER payment success
    with get_session() as db:
        order = Order(
            buyer_id=buyer_id,
            seller_id=seller_id,
            amount_cents=amount_cents,
            currency=currency,
            paid=True
        )

        db.add(order)
        db.commit()
        db.refresh(order)

    return {
        "order_id": order.id,
        "paid_via": "Tide UK" if buyer_country == "UK" else "Internal",
        "fees": fees
    }
