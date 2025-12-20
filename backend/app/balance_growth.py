from app.db import get_session
from app.models import Wallet
from app.ledger import record_ledger_entry

def apply_balance_growth():
    """
    Applies 0.1% growth to balances held over time.
    """

    with get_session() as db:
        wallets = db.query(Wallet).all()

        for wallet in wallets:
            if wallet.balance_cents > 0:
                growth = int(wallet.balance_cents * 0.001)
                record_ledger_entry(wallet.user_id, growth, wallet.currency, "balance_growth")
