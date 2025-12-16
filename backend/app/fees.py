# backend/app/fees.py
# This file calculates all platform fees

def calculate_fees(amount_cents: int):
    """
    Calculates platform fees for an order.

    Business rules:
    - 25% transaction fee
    - £2 admin fee (200 pence)
    """

    # Calculate 25% transaction fee
    transaction_fee = int(amount_cents * 0.25)

    # Fixed admin fee (£2)
    admin_fee = 200

    # Amount seller receives after fees
    seller_receives = amount_cents - transaction_fee - admin_fee

    # Return all values as a dictionary
    return {
        "transaction_fee": transaction_fee,
        "admin_fee": admin_fee,
        "seller_receives": seller_receives
    }
