from pybit.unified_trading import HTTP


session = HTTP(
    testnet=True,
    api_key="Cipei97U5fwGG3FLxa",
    api_secret="sV8A3fi8m7yxq3RJWNllPVaD9dPfKj9w0mkw",)

coinspot = ['ETHUSDT','SOLUSDT','BTCUSDT','MNTUSDT','XRPUSDT','STRKUSDT','ONDOUSDT','BNBUSDT','ETCUSDT']

def get_price():
    for coin in coinspot:
        response = session.get_tickers(
            category="linear",
            symbol=f"{coin}",)['result']['list'][0]['markPrice']
        
        yield f"{coin}: {response}\n"

coinsprice = list(get_price())

price_for_print = ''

for coin_price in coinsprice:
    price_for_print += coin_price

print(price_for_print)











