from dash import dcc
from dash import html
import plotly.express as px
from utils.sp500 import get_tickers
from utils.yahoo import TickerData
from utils.constants import MARKS


df = TickerData("VTR").get_prices()
fig = px.line(df["Close"])
options = [
    {"label": i[1]["Security"], "value": i[1]["Symbol"]}
    for i in get_tickers().iterrows()
]


layout = html.Div(
    [
        html.H1("Dash financial dashboard example"),
        html.Label(" Select dropdown"),
        dcc.Dropdown(
            id="stock-name-dropdown", options=options, value="VTR", className="dropdown"
        ),
        html.Div(
            id="dynamic-tables-container",
            children=[],
        ),
        html.Div(
            children=[
                dcc.Graph(id="prices-chart", figure=fig),
                dcc.Slider(
                    id="year-slider",
                    min=1,
                    max=6,
                    value=1,
                    marks=MARKS,
                    step=1,
                ),
            ]
        ),
        html.Div(id="dynamic-charts-container", children=[]),
    ]
)
