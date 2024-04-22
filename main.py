# Import pybit and define the HTTP object.
from pybit.unified_trading import HTTP
import time
from datetime import datetime, timedelta
import logging

# импорт другого файла целиком
import support

session = HTTP(
    testnet=False,
    api_key="MWvHnQQH3kgWD32o6P",
    api_secret="gByweE1l74shCdBxCte8lX66QgDZh6r7L0aL",
    recv_window = 6000,
    return_response_headers = True
)

def buy_something(ticker, amount, leverage):
    operation_result = session.place_order(
    category = "linear",
    symbol = "ENAUSDT",
    side = "Buy",
    # Очень важное место! По умолчанию Buy ордера подразумевают в qty USDT, а Sell ордера подразумевают базовую валюту!
    # Поэтому чтобы случайно не влететь в шорт на 10 биткоинов вместо 10 usdt, нужно всегда жестко указывать этот параметр
    # Чтобы всегда контролировать что и там и там у нас расчеты в USDT
    marketUnit = "quoteCoin", #USDT
    qty = "10",
    orderType = "Market"
)
    print(f"Buying {amount} of {ticker} with leverage {leverage}")

# Начальное время
start_time = datetime.now()

time_elapsed_balance = datetime.now()
time_elapsed_operations = datetime.now()

time_start_balance = datetime.now()
time_start_operations = datetime.now()

query_period_balance = timedelta(seconds=3)
query_period_positions = timedelta(seconds=6)

# Цикл, который будет выполняться каждые 5 секунд
while True:
    current_time = datetime.now()
    time_elapsed_balance = current_time - time_start_balance
    time_elapsed_operations = current_time - time_start_operations

    time_elapsed_operations
    # Запрос баланса с заданной периодичностью
    if time_elapsed_balance >= query_period_balance:
        # Установить новое начальное время
        time_start_balance = current_time
        
        balance_response = session.get_wallet_balance(
        accountType = "UNIFIED"
        )

        total_wallet_balance = balance_response[0]["result"]["list"][0]["totalEquity"]
        # print("Total Wallet Balance:", round(float(total_wallet_balance)*93,9))
        print("Total Wallet Balance:", total_wallet_balance)


    else:
        time.sleep(1)  # Если не прошло 5 секунд, подождать 1 секунду




# response = session.get_orderbook(category = "linear", symbol = "BTCUSDT")

# print(session.get_wallet_balance(accountType = "UNIFIED"))


# print (response)

