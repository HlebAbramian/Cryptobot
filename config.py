from pybit.unified_trading import HTTP
import time


session = HTTP(
    testnet=False,
    api_key="api_key",
    api_secret="api_secret",)

coin_spot = ['BTCUSDT','ETHUSDT','SOLUSDT','MNTUSDT','XRPUSDT','STRKUSDT','ONDOUSDT','BNBUSDT','ETCUSDT']

def get_price(coins_list):
    prices = {}
    for coin in coins_list:
        response = session.get_tickers(
            category="linear",
            symbol=f"{coin}",)['result']['list'][0]['markPrice']
        
        prices[coin] = response
    
    return prices

current_price = get_price(coin_spot)

price_for_print = ''.join([f"{coin}: {price}\n" for coin, price in current_price.items()])

print(''.join(price_for_print))

time.sleep(10)
new_price = get_price(coin_spot)
price_for_print = ''.join([f"{coin}: {price}\n" for coin, price in new_price.items()])
print(''.join(price_for_print))

def percent(current_price, new_price):
    price_change_list = []
    for coin, price in current_price.items():
        cur_price = float(current_price[coin])
        nw_price = float(new_price[coin])
        price_change = ((cur_price - nw_price) / cur_price) * 100
        price_change = round(price_change,5)
        price_change_list += f"Change of {coin}: {price_change}%\n"
    return (price_change_list)

print(''.join(percent(current_price,new_price)))








