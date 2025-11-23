#!/usr/bin/env python3
"""
Example: How to use binance-timestamp-fix with UMFutures
"""

from binance.um_futures import UMFutures
from binance_timestamp_fix import apply_timestamp_fix

# Replace with your keys (use testnet for safety!)
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"

# Create client (testnet recommended during testing)
client = UMFutures(
    key=API_KEY,
    secret=API_SECRET,
    base_url="https://testnet.binancefuture.com"  # Remove for real account
)

# ← THIS IS THE ONLY LINE YOU NEED
apply_timestamp_fix(client, offset_seconds=5.0)

print("Getting account balance...")
try:
    account = client.account()
    usdt = next(a for a in account["assets"] if a["asset"] == "USDT")
    print(f"Available USDT: {usdt['availableBalance']}")
except Exception as e:
    print(f"Error: {e}")

# To disable later (optional):
# from binance_timestamp_fix import disable_timestamp_fix
# disable_timestamp_fix()
