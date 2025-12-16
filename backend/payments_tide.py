# backend/app/payments_tide.py
# Handles UK payments using Tide (simulated for free version)

def process_tide_payment(user_id: int, amount_cents: int):
    """
    Simulates a Tide UK payment.

    In production:
    - Call Tide API
    - Verify payment reference
    - Confirm funds received

    FREE VERSION:
    - Always returns success
    """

    # Simulated Tide transaction ID
    tide_transaction_id = f"TIDE-{user_id}-{amount_cents}"

    return {
        "success": True,
        "tide_tx_id": tide_transaction_id
    }
