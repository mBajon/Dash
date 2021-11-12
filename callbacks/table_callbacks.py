import dash
from dash.dependencies import Input, Output, State, MATCH
import plotly.express as px
from app import app
from layouts.layouts import df
from layouts.table_layouts import generate_table
from utils.yahoo import TickerData
from utils.constants import GENERAL_INFO, TRADING_DATA
from dash import html


@app.callback(
    Output("dynamic-tables-container", "children"),
    Input(component_id="stock-name-dropdown", component_property="value"),
    State("dynamic-tables-container", "children"),
)
def display_tables(selected_stock, children):
    new_element = html.Div(
        [
            html.Div(
                generate_table(
                    TickerData(selected_stock).get_basic_info(TRADING_DATA),
                    ["Trading Data"],
                ),
                className="table-div-wrapper",
            ),
            html.Div(
                generate_table(
                    TickerData(selected_stock).get_basic_info(GENERAL_INFO),
                    ["General Info"],
                ),
                className="table-div-wrapper",
            ),
            html.Div(
                generate_table(TickerData(selected_stock).get_returns(), ["Returns"]),
                className="table-div-wrapper",
            ),
        ]
    )
    return new_element
