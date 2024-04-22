from pybit.unified_trading import HTTP
import time
from datetime import datetime, timedelta
import json

session = HTTP(
    testnet=False,
    api_key="MWvHnQQH3kgWD32o6P",
    api_secret="gByweE1l74shCdBxCte8lX66QgDZh6r7L0aL",
    return_response_headers = True
)

# response = session.get_orderbook(category = "linear", symbol = "BTCUSDT")
balance_response = session.get_wallet_balance(
    accountType = "UNIFIED"
)
positions_response = session.get_positions(
    category="linear",
    symbol="AVAXUSDT",
)
BTC_kline = session.get_kline(
    category="linear",
    symbol="BTCUSD",
    interval=60,
    start=1670601600000,
    end=1670608800000,
)

total_wallet_balance = balance_response[0]["result"]["list"][0]["totalEquity"]
PnL = balance_response[0]["result"]["list"][0]["totalPerpUPL"]

position_data = positions_response[0]["result"]["list"][0]["unrealisedPnl"]

print("Total Wallet Balance:", round(float(total_wallet_balance)*92,0))
print("Positions:", position_data)
# print("KLine:", BTC_kline)
print("PnL Realised:", PnL)

