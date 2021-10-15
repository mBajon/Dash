from dash import dcc
from dash import html
import plotly.express as px
import dash_table
from utils.sp500 import get_tickers
from utils.yahoo import TickerData
from layouts.table_layouts import generate_table
import dash_bootstrap_components as dbc


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
                                                marks={
                                                        1: {'label': '5y'},   
                                                        2: {'label': '3y'},
                                                        3: {'label': '1y'}, 
                                                        4: {'label': '6m'},
                                                        4: {'label': '3m'},
                                                        5: {'label': '1m'},
                                                        6: {'label': '7d'}
                                                },
                                                step=1,
                                    )
                    ])              
])