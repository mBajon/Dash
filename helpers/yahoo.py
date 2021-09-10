from re import T
from pandas.core.frame import DataFrame
import yfinance as yf
import datetime
from dateutil.relativedelta import relativedelta


class TickerData():

    def __init__(self, ticker: str) -> None:
        self.ticker = yf.Ticker(ticker)

    def get_prices(self, start: datetime= None , end: datetime=None) -> DataFrame:
        if end is None:
            end = datetime.date.today()
        if start is None:
            start = end - relativedelta(years=5)
        
        return self.ticker.history(period='1d', start=start, end=end)

    def get_basic_info(self, field):
        return self.ticker.info[field]


print(TickerData("VTR").get_basic_info('sector'))


