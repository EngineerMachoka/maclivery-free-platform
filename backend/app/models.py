from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

# ---------------- USERS ----------------
class User(SQLModel, table=True):
    """
    Represents a system user (buyer, seller, admin).
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    country: str  # "UK" or "KE"

# ---------------- WALLETS ----------------
class Wallet(SQLModel, table=True):
    """
    Stores balances per user per currency.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    currency: str  # GBP or KES
    balance_cents: int = 0

# ---------------- ORDERS ----------------
class Order(SQLModel, table=True):
    """
    Represents a paid marketplace order.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    buyer_id: int
    seller_id: int
    amount_cents: int
    currency: str
    paid: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)

# ---------------- LEDGER ----------------
class LedgerEntry(SQLModel, table=True):
    """
    Records every money movement in the system.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    amount_cents: int
    currency: str
    reason: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
