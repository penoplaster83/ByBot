# Import pybit and define the HTTP object.
from pybit.unified_trading import HTTP

"""
You can create an authenticated or unauthenticated HTTP session. 
You can skip authentication by not passing any value for api_key
and api_secret.
"""
session = HTTP(
    testnet=True,
    api_key="...",
    api_secret="...",
)

print("hello")

