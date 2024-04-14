# Import pybit and define the HTTP object.
from pybit.unified_trading import HTTP

"""
You can create an authenticated or unauthenticated HTTP session. 
You can skip authentication by not passing any value for api_key
and api_secret.
"""
session = HTTP(
    testnet=False,
    api_key="MWvHnQQH3kgWD32o6P",
    api_secret="gByweE1l74shCdBxCte8lX66QgDZh6r7L0aL",
)

response = session.get_orderbook(category = "linear", symbol = "BTCUSDT")
print(session.get_wallet_balance(accountType = "UNIFIED"))

print (response)

