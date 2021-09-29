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

    def get_basic_info(self, info:list) -> dict:
        return {i : self.ticker.info[i] for i in info}
    
    def get_returns(self):
        df = self.get_prices()
        time_frames = ['7d','1m','3m','6m','1y','3y','5y']
        returns = {}
        for tf in time_frames:
            dff=df.last(tf)
            returns[tf]=("{:.2%}".format((dff["Close"].iloc[-1] / dff["Close"].iloc[0]) - 1))

        return returns
        
