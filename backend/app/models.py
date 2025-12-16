# backend/app/models.py
# This file defines database tables (data models)

# Import SQLModel base class and Field helper
from sqlmodel import SQLModel, Field

# Used for optional fields (nullable)
from typing import Optional

# Used to store timestamps
from datetime import datetime

class User(SQLModel, table=True):
    """
    Represents a platform user.
    A user can be a customer, seller, or admin.
    """
    # Primary key (auto-incremented)
    id: Optional[int] = Field(default=None, primary_key=True)

    # Role defines permissions
    role: str  # customer | seller | admin

    # Country determines currency and branch logic
    country: str  # KE | UK

class Wallet(SQLModel, table=True):
    """
    Stores money balances for each user.
    Balances are stored in cents to avoid rounding errors.
    """
    id: Optional[int] = Field(default=None, primary_key=True)

    # Links wallet to a user
    user_id: int

    # Currency of the wallet
    currency: str  # KES | GBP

    # Balance stored as integer cents
    balance_cents: int = 0

class Order(SQLModel, table=True):
    """
    Represents a marketplace order.
    Orders must be PAID before they are created.
    """
    id: Optional[int] = Field(default=None, primary_key=True)

    # Buyer placing the order
    buyer_id: int

    # Seller receiving the order
    seller_id: int

    # Order value in cents
    amount_cents: int

    # Currency used for this order
    currency: str

    # Indicates whether payment was completed
    paid: bool = False

    # Timestamp when order was created
    created_at: datetime = Field(default_factory=datetime.utcnow)
