from dash import dcc
from dash import html
import plotly.express as px
import dash_table
from utils.sp500 import get_tickers
from utils.yahoo import TickerData
from layouts.table_layouts import generate_table
from layouts.bar_chart_layouts import bar_chart
import dash_bootstrap_components as dbc
from utils.constants import MARKS



df = TickerData("VTR").get_prices()
fig = px.line(df["Close"])
options = [{'label':i[1]['Security'],'value':i[1]['Symbol']} for i in get_tickers().iterrows()]



layout=html.Div([
                html.Label(' Select dropdown'),
                dcc.Dropdown(id="stock-name-dropdown",
                               options=options,
                               value='VTR',
                               style={'width':'40%'}),
                html.Div(           
                         id='dynamic-tables-container', children = [],
                ),
                html.Div(children=[
                                    dcc.Graph(id='prices-chart',figure=fig),
                                    dcc.Slider(
                                                id='year-slider',
                                                min=1,
                                                max=6,
                                                value=1,
                                                marks=MARKS,
                                                step=1,
                                    )
                    ]),
                bar_chart                 
])