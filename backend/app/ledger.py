from app.db import get_session
from app.models import LedgerEntry, Wallet

def record_ledger_entry(user_id, amount_cents, currency, reason):
    """
    Writes a ledger entry and updates wallet balance.
    """

    with get_session() as db:
        # Create ledger record
        entry = LedgerEntry(
            user_id=user_id,
            amount_cents=amount_cents,
            currency=currency,
            reason=reason
        )
        db.add(entry)

        # Get or create wallet
        wallet = db.query(Wallet).filter(
            Wallet.user_id == user_id,
            Wallet.currency == currency
        ).first()

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
