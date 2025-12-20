from fastapi import FastAPI
from app.orders import create_order
from app.dashboard import wallet_dashboard, ledger_dashboard
from app.admin import admin_summary

app = FastAPI()

@app.post("/orders")
def place_order(buyer_id: int, seller_id: int, amount_cents: int, currency: str, buyer_country: str):
    return create_order(buyer_id, seller_id, amount_cents, currency, buyer_country)

@app.get("/dashboard/{user_id}/wallets")
def wallets(user_id: int):
    return wallet_dashboard(user_id)

@app.get("/dashboard/{user_id}/ledger")
def ledger(user_id: int):
    return ledger_dashboard(user_id)

@app.get("/admin/summary")
def admin():
    return admin_summary()
