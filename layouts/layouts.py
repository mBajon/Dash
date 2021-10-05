from constants import COLUMNS, STYLE_CELL_CONDITIONAL, TABLE_STYLE, DATABLE_STYLE
from dash import dcc
from dash import html
import plotly.express as px
import dash_table
from helpers.sp500 import get_tickers
from helpers.yahoo import TickerData
from layouts.table_layouts import generate_table


df = TickerData("VTR").get_prices()
fig = px.line(df["Close"])
options = [{'label':i,'value':i} for i in dict(get_tickers()).values()]



layout=html.Div([
                    html.Label(' Select dropdown'), 
                    dcc.Dropdown(id="stock-name-dropdown",
                    options=options,
                    value='VTR'),
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
                                                    generate_table(TickerData("VTR").get_basic_info(['country','exchange', 'sector', 'fullTimeEmployees', 'marketCap']), ['key','value']),
                                                    style=TABLE_STYLE,id='basic_info'
                                                    ),
                                            html.Div(           
                                                    generate_table(TickerData("VTR").get_returns(),  ['range','returns']),
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