
import dash
from dash.dependencies import Input, Output
import plotly.express as px
from app import app
from layouts.layouts import df
from layouts.table_layouts import generate_table
from utils.yahoo import TickerData

@app.callback(
    Output(component_id='returns', component_property='children'),
    Input(component_id='stock-name-dropdown', component_property='value')
    ) 
def update_table(selected_stock):
    return generate_table(TickerData(selected_stock).get_returns(),  ['Returns'])

@app.callback(
    Output(component_id='basic_info', component_property='children'),
    Input(component_id='stock-name-dropdown', component_property='value')
    ) 
def update_table(selected_stock):
    return generate_table(TickerData(selected_stock).get_basic_info(['longName','country','exchange', 'sector','industry', 'fullTimeEmployees', 'marketCap']), ['General Info'])

@app.callback(
    Output(component_id='price_action', component_property='children'),
    Input(component_id='stock-name-dropdown', component_property='value')
    ) 
def update_table(selected_stock):
    return generate_table(TickerData(selected_stock).get_basic_info(['fiftyTwoWeekHigh','fiftyTwoWeekLow','fiftyDayAverage', 'regularMarketVolume','averageDailyVolume10Day', 'volume24Hr']), ['Trading Data'])