
from numpy import string_
from pandas.core.frame import DataFrame
import yfinance as yf
import datetime

def get_prices(ticker : str = "", start: datetime= None , end: datetime=None) -> DataFrame:
    if end is None:
        end = datetime.date.today()
    if start is None:
        start = end - datetime.timedelta(days=600)

    return yf.Ticker(ticker).history(period='1d', start=start, end=end)




