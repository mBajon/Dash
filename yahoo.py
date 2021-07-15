from pandas.core.frame import DataFrame
import yfinance as yf
import datetime
from dateutil.relativedelta import relativedelta

def get_prices(ticker : str = "", start: datetime= None , end: datetime=None) -> DataFrame:
    if end is None:
        end = datetime.date.today()
    if start is None:
        start = end - relativedelta(years=5)

    return yf.Ticker(ticker).history(period='1d', start=start, end=end)
