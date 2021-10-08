from utils.constants import COLUMNS, STYLE_CELL_CONDITIONAL, TABLE_STYLE, DATABLE_STYLE
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
                    html.Div(children=[
                        html.H4(id='table-title'),
                            html.Div(children=[
                                    html.Div(                   
                                        dash_table.DataTable(
                                            id='table',
                                            columns=COLUMNS,
                                            data=df.to_dict('records'),
                                            page_size=10,
                                            style_cell_conditional=STYLE_CELL_CONDITIONAL,
                                            style_table = {'display': 'inline-block'}
                                                    ),
                                            style=DATABLE_STYLE
                                            ),
                                            html.Div(           
                                                    style=TABLE_STYLE,id='basic_info'
                                                    ),
                                            html.Div(           
                                                    style=TABLE_STYLE,id='price_action'
                                                    ),
                                            html.Div(           
                                                    style=TABLE_STYLE,
                                                    id='returns')
                                                ]),
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