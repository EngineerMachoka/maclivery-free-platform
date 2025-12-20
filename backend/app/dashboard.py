from app.db import get_session
from app.models import Wallet, LedgerEntry

def wallet_dashboard(user_id):
    """
    Returns user balances.
    """
    with get_session() as db:
        return db.query(Wallet).filter(Wallet.user_id == user_id).all()

def ledger_dashboard(user_id):
    """
    Returns user transaction history.
    """
    with get_session() as db:
        return db.query(LedgerEntry).filter(LedgerEntry.user_id == user_id).all()
