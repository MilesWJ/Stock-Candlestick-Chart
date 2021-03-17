import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import datetime as dt
from stock import Stock


def stock_chart():

    Stock.stockticker = str(input("\nEnter the stock ticker: ")).upper()
    Stock.finance_api = str(input("Enter the finance API: "))

    start_date = str(input("\nEnter the starting date (EX: YYYY/MM/DD): "))
    end_date = str(input("Enter the ending date (EX: YYYY/MM/DD): "))

    start_year = int(start_date[0:4])
    start_month = int(start_date[5:7])
    start_day = int(start_date[8:10])

    end_year = int(end_date[0:4])
    end_month = int(end_date[5:7])
    end_day = int(end_date[8:10])

    Stock.start = dt.datetime(start_year, start_month, start_day)
    Stock.end = dt.datetime(end_year, end_month, end_day)

    data = web.DataReader(
        Stock.stockticker, Stock.finance_api, Stock.start, Stock.end)

    def set_up():

        COLORS = mpf.make_marketcolors(
            up="#00ff00", down="#ff0000", wick="inherit", edge="inherit", volume="in")
        STYLE = mpf.make_mpf_style(
            base_mpf_style="nightclouds", marketcolors=COLORS)
        TITLE = f"\n{Stock.stockticker} CANDLESTICK STOCK CHART"

        print(f"\nCreating {Stock.stockticker} candlestick stock chart...")

        mpf.plot(data, type="candle", style=STYLE, volume=True, title=TITLE)

        print(f"Closing {Stock.stockticker} candlestick stock...")

    set_up()


while True:
    stock_chart()
