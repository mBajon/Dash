import dash_html_components as html
from dash import dcc
import plotly.express as px
from utils.yahoo import TickerData

def generate_bar_chart():
    bar_chart = html.Div([
        html.Div(
            dcc.Graph(id = {'type': 'dynamic-bar-chart', index:'earnings-chart'}, 
            figure = chart),
            className = 'chart-div-wrapper'
    ),
        html.Div(
            dcc.Graph(id = {'type': 'dynamic-bar-chart', index:'reccomendations-chart'}, 
            figure = recomendations_chart),
            className = 'chart-div-wrapper'
    )])
    return bar_chart