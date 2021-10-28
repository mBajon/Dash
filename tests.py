import yfinance as yf
import plotly.express as px
from utils.yahoo import TickerData
import dash_core_components as dcc
from datetime import date
import numpy as np
# x = np.datetime64(date(date.today().year, 1, 1))
# print(x)
#msft = yf.Ticker("MSFT")
#print(msft.recommendations)
#print(date(date.today().year, 1, 1))#
#print(TickerData("MSFT").get_recommendations())


#print(px.data.iris())
#df = px.data.iris()  # iris is a pandas DataFrame

#fig = px.scatter(df, x="sepal_width", y="sepal_length")

#dcc.Graph(figure=fig)
# df  = TickerData("MSFT").get_earnings()
# print(df)

