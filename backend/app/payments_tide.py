def process_tide_payment(user_id: int, amount_cents: int):
    """
    Simulates a Tide UK payment.
    In production, this would call Tide's API.
    """

    # Always return success in free version
    return {
        "success": True,
        "reference": f"TIDE-{user_id}-{amount_cents}"
    }
