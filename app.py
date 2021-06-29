import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Tr import Tr
import plotly.express as px
import pandas as pd
from sp500 import get_tickers
from yahoo import get_prices

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWlwgP.css']
app= dash.Dash(__name__, external_stylesheets=external_stylesheets)

options = [{'label':i,'value':i} for i in dict(get_tickers()).values()]
df = get_prices("VTR")


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ],id="prices-table")

fig = px.line(get_prices("VTR")["Close"])


app.layout=html.Div([
                    html.Label('Dropdown'),
                    dcc.Dropdown(id="stock-name-dropdown",
                    options=options,
                    value='mtl'),
                    html.Label('Select Dropdown'),
                    html.Div(children=[
                    html.H4(id='table-title'),
                    generate_table(df),
                    dcc.Graph(id='prices-chart',
                    figure=fig)
                    
])
])

@app.callback([
    Output(component_id='table-title', component_property='children'),
    Output('prices-table', 'children'),
    Output('prices-chart', 'figure')],
    Input(component_id='stock-name-dropdown', component_property='value')
)
def update_table_title(selected_stock):
    filtered_df = get_prices(selected_stock)
    price_table = generate_table(filtered_df)
    fig = px.line(filtered_df["Close"])
    fig.update_layout(transition_duration=500)

    return 'Prices of: {}'.format(selected_stock), price_table, fig


if __name__=='__main__':
    app.run_server(debug=True)




