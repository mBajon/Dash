from re import T
from pandas.core.frame import DataFrame
import yfinance as yf
import datetime
from datetime import date
import numpy as np
from dateutil.relativedelta import relativedelta
from utils.constants import FIELD_MAP
from utils.constants import FORMAT_MAP
from utils.constants import GENERAL_INFO
import locale

locale.setlocale(locale.LC_ALL, "en_US")


class TickerData:
    def __init__(self, ticker: str) -> None:
        self.ticker = yf.Ticker(ticker)

    def get_prices(self, start: datetime = None, end: datetime = None) -> DataFrame:
        if end is None:
            end = datetime.date.today()
        if start is None:
            start = end - relativedelta(years=5)

        return self.ticker.history(period="1d", start=start, end=end)

    def get_basic_info(self, info: list) -> dict:
        new_info = self.format_fields(self.ticker.info, FORMAT_MAP)
        return {FIELD_MAP[i]: new_info[i] for i in info if i in FIELD_MAP}

    def get_returns(self, df: DataFrame = None) -> DataFrame:
        if df is None:
            df = self.get_prices()
        else:
            df = df

        time_frames = ["7d", "1m", "3m", "6m", "1y", "3y", "5y"]
        returns = {}
        for tf in time_frames:
            dff = df.last(tf)
            returns[tf] = "{:.2%}".format(
                (dff["Close"].iloc[-1] / dff["Close"].iloc[0]) - 1
            )

        return returns

    def get_earnings(self) -> DataFrame:
        return self.ticker.earnings

    def get_recommendations(self) -> DataFrame:
        df = self.ticker.recommendations
        this_year_start = np.datetime64(date(date.today().year, 1, 1))
        return (
            df[df.index > this_year_start]
            .groupby(["To Grade"])
            .size()
            .reset_index(name="counts")
        )

    def format_fields(self, dictionary: dict, mapping: dict()) -> dict():
        dictionary = dictionary
        mapping = mapping
        for i in dictionary:
            if i in mapping:
                if mapping[i] == "Currency":
                    dictionary[i] = locale.currency(dictionary[i], grouping=True)
                if mapping[i] == "Number":
                    dictionary[i] = f"{dictionary[i]:,}"

        return dictionary
