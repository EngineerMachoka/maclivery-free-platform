@app.post("/orders")
def place_order(
    buyer_id: int,
    seller_id: int,
    amount_cents: int,
    currency: str,
    buyer_country: str
):
    """
    Creates an order with country-based payment enforcement.
    """

    return create_order(
        buyer_id=buyer_id,
        seller_id=seller_id,
        amount_cents=amount_cents,
        currency=currency,
        buyer_country=buyer_country
    )
