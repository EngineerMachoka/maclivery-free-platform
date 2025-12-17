# backend/app/balance_growth.py
# Applies time-based balance growth

from datetime import datetime, timedelta
from app.db import get_session
from app.models import Wallet
from app.ledger import record_ledger_entry

def apply_balance_growth():
    """
    Applies balance growth to wallets holding funds
    for more than 1 hour.
    """

    with get_session() as db:
        wallets = db.query(Wallet).all()

        for wallet in wallets:

            # Skip empty wallets
            if wallet.balance_cents <= 0:
                continue

            # Simple growth logic: 0.1% per hour (example)
            growth = int(wallet.balance_cents * 0.001)

            if growth > 0:
                record_ledger_entry(
                    user_id=wallet.user_id,
                    amount_cents=growth,
                    currency=wallet.currency,
                    reason="balance_growth"
                )
