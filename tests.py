import itertools
import unittest
import sys
import pandas as pd
import numpy as np
import pandas.api.types as ptypes
from pandas.testing import assert_frame_equal
from pandas import util
from pandas.tseries.offsets import BDay

sys.path.append("../")
from utils.yahoo import TickerData
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
import datetime
from pandas import DataFrame
from utils.constants import EXPECTED_RESULTS


class TickerDataTestCase(unittest.TestCase):
    def test_TickerData(self):
        self.Test_TickerData = TickerData("VTR")
        self.assertIsInstance(self.Test_TickerData, TickerData)

    def test_price_data_not_empty(self):
        data = TickerData("VTR").get_prices()
        self.assertNotEqual(len(data), 0)

    def test_price_data_has_close_column(self):
        data = TickerData("VTR").get_prices()
        self.assertEqual("Close" in data.columns, True)

    def test_close_price_type(self):
        assert ptypes.is_float_dtype(TickerData("VTR").get_prices()["Close"])

    def test_index_column_type_is_datetime(self):
        assert ptypes.is_datetime64_any_dtype(TickerData("VTR").get_prices().index)

    def test_correct_price_date_range(self):
        start = pd.Timestamp(2020, 1, 2)
        end = pd.Timestamp(2020, 12, 31, 0, 0, 0)
        df = TickerData("VTR").get_prices(start, end)
        self.assertAlmostEqual(df.index[0], start)
        self.assertAlmostEqual(df.index[-1], end - datetime.timedelta(days=1))

    def test_basic_info_columns(self):
        TEST_COLUMNS = ["fiftyTwoWeekHigh", "fiftyTwoWeekLow", "longName"]
        EXPECTED_COLUMNS = ["52 Week High", "52 Week Low", "Name"]
        data = TickerData("VTR").get_basic_info(TEST_COLUMNS)
        keys = list(data.keys())
        self.assertIsInstance(data, dict)
        self.assertListEqual(keys, EXPECTED_COLUMNS)

    def test_get_earnings(self):
        data = TickerData("VTR").get_earnings()
        self.assertIsInstance(data, pd.DataFrame)
        assert "Revenue" in list(data.columns)
        assert "Earnings" in list(data.columns)

    def test_get_recommendations(self):
        data = TickerData("VTR").get_recommendations()
        assert "To Grade" in list(data.columns)
        assert "counts" in list(data.columns)
        assert ptypes.is_object_dtype(data["To Grade"])
        assert ptypes.is_int64_dtype(data["counts"])
        self.assertIsInstance(data, pd.DataFrame)

    def test_ticker_returns(self):

        end = datetime.date.today()
        start = end - relativedelta(years=5)
        index = pd.date_range(start=start, end=end)
        FRAMES = ["7d", "1m", "3m", "6m", "1y", "3y", "5y"]

        df = DataFrame(
            data=np.random.randint(0, 100, len(index)), index=index, columns=["Close"]
        )
        df.iloc[-1] = 1

        for i in FRAMES:
            y = df.last(i).index[0]
            df.loc[y, ["Close"]] = 1

        results = TickerData("VTR").get_returns(df)
        self.assertDictEqual(results, EXPECTED_RESULTS)


if __name__ == "__main__":
    unittest.main()
