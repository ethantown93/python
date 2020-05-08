def stocks():
    stocks = {
        "MSFT": 178.60,
        "WMT": 132.12,
        "JNJ": 152.02,
        "INTC": 60.36,
        "PG": 124.69,
        "UNH": 290.56,
        "AAPL": 282.80,
        "HD": 209.42,
        "VZ": 58.46,
        "PFE": 36.91
    }

    user_input = input('Please enter a stock ticker: ')

    if user_input in stocks:
        print(f"""The current value of {user_input} is ${stocks[user_input]}.""")
    if user_input not in stocks:
        print('Stock ticker not found, please try again.') 


stocks()

