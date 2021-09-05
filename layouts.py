from constants import COLUMNS, STYLE_CELL_CONDITIONAL
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Tr import Tr
import plotly.express as px
import dash_table
from sp500 import get_tickers
from yahoo import get_prices


df = get_prices("VTR")


fig = px.line(df["Close"])

options = [{'label':i,'value':i} for i in dict(get_tickers()).values()]

layout=html.Div([
                    html.Label('Dropdown'),
                    dcc.Dropdown(id="stock-name-dropdown",
                    options=options,
                    value='vtr'),
                    html.Label('Select Dropdown'),
                    html.Div(children=[
                    html.H4(id='table-title'),
                    html.Div(
                    dash_table.DataTable(
                                        id='table',
                                        columns=COLUMNS,
                                        data=df.to_dict('records'),
                                        page_size=10,
                                        style_cell_conditional=STYLE_CELL_CONDITIONAL
                                        ),
                                        style = {
                                        "width":"800px"
                                        }
                            ),
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
]
)