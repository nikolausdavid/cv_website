import pandas as pd
import numpy as np
from yahooquery import Ticker
import yfinance as yf
from datetime import date, timedelta

today = date.today()
start_date = date.today() - timedelta(weeks=27)
start_date = f"{start_date.year}-{start_date.month}-{start_date.day}"
today = f"{today.year}-{today.month}-{today.day}"
momentum_start = date.today() - timedelta(weeks=4)
momentum_start = f"{momentum_start.year}-{momentum_start.month}-{momentum_start.day}"

def compass(stocks):
    _data_points = ["Stock","Momentum", "Levy"]
    updated_stocks = []
    for stock in stocks:
        if len(pd.DataFrame(yf.Ticker(stock).history(start=start_date))["Close"]) != 0:
            updated_stocks.append(stock)
        else:
            pass
    data = pd.DataFrame({"Stock": updated_stocks, "Momentum": None, "Levy": None}, index=updated_stocks)
    for stock in updated_stocks:
        data.loc[stock]["Stock"] = pd.DataFrame(sp500_raw).set_index(sp500_raw["Symbol"]).loc[stock]["Security"]
        data.loc[stock]["Momentum"] = momentum(stock)
        data.loc[stock]["Levy"] = relative_strength(stock)
    return data
      
def relative_strength(stock, start=start_date):
    constructor = pd.DataFrame(yf.Ticker(stock).history(start=start))
    strength = constructor["Close"][-1] / np.mean(constructor["Close"][:-1])
    return strength

def momentum(stock, start=momentum_start):
    constructor = pd.DataFrame(yf.Ticker(stock).history(start=start))
    moment = constructor["Close"][-1] / constructor["Close"][0]
    return moment