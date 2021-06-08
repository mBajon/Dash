import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Tr import Tr
import plotly.express as px
import pandas as pd
from sp500 import get_tickers
from yahoo import get_prices

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWlwgP.css']
app= dash.Dash(__name__, external_stylesheets=external_stylesheets)

options = [{'label':i,'value':i} for i in dict(get_tickers()).values()]
df = get_prices("VTR")


def generate_table(dataframe, max_rows=102):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app.layout=html.Div([html.Label('Dropdown'),
                    dcc.Dropdown(
                    options=options,
                    value='mtl'),
                    html.Label('Select Dropdown'),
                    html.Div(children=[
                    html.H4(children='Prices of VTR'),
                    generate_table(df)
])

])

if __name__=='__main__':
    app.run_server(debug=True)


