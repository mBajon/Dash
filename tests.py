import yfinance as yf

from utils.yahoo import TickerData

msft = yf.Ticker("MSFT")
print(msft.earnings)
print(TickerData("MSFT").get_earnings())

