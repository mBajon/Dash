from constants import COLUMNS, STYLE_CELL_CONDITIONAL
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Tr import Tr
import plotly.express as px
import dash_table
from helpers.sp500 import get_tickers
from helpers.yahoo import TickerData
#from callbacks.callbacks import generate_table


df = TickerData("VTR").get_prices()


fig = px.line(df["Close"])

options = [{'label':i,'value':i} for i in dict(get_tickers()).values()]

def generate_table(data, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in data.keys()])
        ),
        html.Tbody([
            html.Tr([
                html.Td(data[col]) for col in  data.keys()
            ])
        ])
    ])

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
                    generate_table(TickerData("VTR").get_basic_info()),
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