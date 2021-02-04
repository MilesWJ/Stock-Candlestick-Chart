class Stock(object):
    def __init__(self, stockticker, finance_api, start, end):
        self.stockticker = stockticker
        self.finance_api = finance_api
        self.start = start
        self.end = end

