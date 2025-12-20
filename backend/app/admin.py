from app.db import get_session
from app.models import LedgerEntry

def admin_summary():
    """
    Returns platform revenue summary.
    """
    with get_session() as db:
        entries = db.query(LedgerEntry).all()
        return {
            "total_entries": len(entries),
            "platform_revenue": sum(
                e.amount_cents for e in entries if e.reason == "platform_fee"
            )
        }
