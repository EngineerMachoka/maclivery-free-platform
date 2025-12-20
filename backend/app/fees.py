def calculate_fees(amount_cents: int):
    """
    Calculates platform fees and seller payout.
    """

    # 25% transaction fee
    transaction_fee = int(amount_cents * 0.25)

    # Fixed admin fee (£2 = 200 cents)
    admin_fee = 200

    # Seller receives remaining amount
    seller_receives = amount_cents - transaction_fee - admin_fee

    return {
        "transaction_fee": transaction_fee,
        "admin_fee": admin_fee,
        "seller_receives": seller_receives
    }
