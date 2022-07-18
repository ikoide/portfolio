import requests

from portfolio.main.models import Prices
from portfolio.extensions import scheduler

@scheduler.task("interval", id="updatePrices", minutes=1, misfire_grace_time=900)
def updatePrices():
    cryptoPrices = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,monero&vs_currencies=usd", timeout=5).json()
    stockOfStonksPrice = round(requests.get("https://api.hypixel.net/skyblock/bazaar", timeout=5).json()["products"]["STOCK_OF_STONKS"]["quick_status"]["sellPrice"], 2)

    if len(Prices.objects()) == 0:
        prices = Prices()
    else:
        prices = Prices.objects().first()

    prices.monero_price = cryptoPrices["monero"]["usd"]
    prices.bitcoin_price = cryptoPrices["bitcoin"]["usd"]
    prices.stock_of_stonks_price = stockOfStonksPrice
    prices.save()

    print("Crypto and Hypixel item prices updated.")
