from dash import html
from dash import dcc
import plotly.express as px
from utils.yahoo import TickerData

def generate_bar_chart(figure, index):
    bar_chart = html.Div(
            dcc.Graph(id = {'type': 'dynamic-bar-chart', 'index':index}, 
            figure = figure),
            className = 'chart-div-wrapper'
    )
    return bar_chart