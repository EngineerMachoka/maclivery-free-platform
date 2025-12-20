# backend/app/wallets.py
# Handles user wallet logic

from app.db import get_session
from app.models import Wallet

def get_or_create_wallet(user_id: int, currency: str):
    """
    Fetch a user's wallet.
    If it does not exist, create it.
    """

    with get_session() as db:
        wallet = db.query(Wallet).filter(
            Wallet.user_id == user_id,
            Wallet.currency == currency
        ).first()

        # Create wallet if missing
        if not wallet:
            wallet = Wallet(
                user_id=user_id,
                currency=currency,
                balance_cents=0
            )
            db.add(wallet)
            db.commit()
            db.refresh(wallet)

        return wallet

def has_sufficient_funds(user_id: int, amount_cents: int, currency: str):
    """
    Checks if user has enough funds.
    """
    wallet = get_or_create_wallet(user_id, currency)
    return wallet.balance_cents >= amount_cents
