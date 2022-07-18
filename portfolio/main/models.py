from portfolio.app import db

class Prices(db.Document):
    monero_price = db.FloatField()
    bitcoin_price = db.FloatField()
    stock_of_stonks_price = db.FloatField()
