# backend/app/ledger.py
# Handles creation of ledger entries and wallet updates

from app.db import get_session
from app.models import LedgerEntry, Wallet

def record_ledger_entry(user_id: int, amount_cents: int, currency: str, reason: str):
    """
    Records a ledger entry and updates wallet balance.
    """

    with get_session() as db:

        # Create ledger entry
        entry = LedgerEntry(
            user_id=user_id,
            amount_cents=amount_cents,
            currency=currency,
            reason=reason
        )
        db.add(entry)

        # Fetch wallet
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

        # Update wallet balance
        wallet.balance_cents += amount_cents

        # Save changes
        db.commit()

        return entry
