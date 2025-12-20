from app.fees import calculate_fees
from app.payments_tide import process_tide_payment
from app.ledger import record_ledger_entry
from app.db import get_session
from app.models import Order

def create_order(buyer_id, seller_id, amount_cents, currency, buyer_country):
    """
    Creates an order only if payment succeeds.
    """

    # UK users must pay via Tide
    if buyer_country == "UK":
        payment = process_tide_payment(buyer_id, amount_cents)
        if not payment["success"]:
            return {"error": "Payment failed"}

    # Calculate fees
    fees = calculate_fees(amount_cents)

    # Buyer pays
    record_ledger_entry(buyer_id, -amount_cents, currency, "order_payment")

    # Seller earns
    record_ledger_entry(seller_id, fees["seller_receives"], currency, "seller_payout")

    # Platform earns (stored in GBP / Tide)
    record_ledger_entry(0, fees["transaction_fee"] + fees["admin_fee"], "GBP", "platform_fee")

    # Save order
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

    return {"status": "Order created"}
