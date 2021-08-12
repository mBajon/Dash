import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Tr import Tr
import dash_table
import plotly.express as px
import pandas as pd
import dash_table.FormatTemplate as FormatTemplate
from sp500 import get_tickers
from yahoo import get_prices

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWlwgP.css']
app= dash.Dash(__name__, external_stylesheets=external_stylesheets)

options = [{'label':i,'value':i} for i in dict(get_tickers()).values()]
df = get_prices("VTR")

columns = [
            {"name": "Open", "id": "Open", 'type': 'numeric','format': FormatTemplate.money(2)},
            {"name": "High", "id": "High", 'type': 'numeric','format': FormatTemplate.money(2)},
            {"name": "Low", "id": "Low", 'type': 'numeric','format': FormatTemplate.money(2)},
            {"name": "Close", "id": "Close", 'type': 'numeric','format': FormatTemplate.money(2)},
            {"name": "Volume", "id": "Volume", 'type': 'numeric'},
            {"name": "Dividends", "id": "Dividends", 'type': 'numeric','format': FormatTemplate.money(2)},
            {"name": "Stock Splits", "id": "Stock Splits", 'type': 'numeric'}
        ]

style_cell_conditional=[
                        {'if': {'column_id': 'Open'},
                        'width': '10%'},
                        {'if': {'column_id': 'High'},
                        'width': '10%'},
                        {'if': {'column_id': 'Low'},
                        'width': '10%'},
                        {'if': {'column_id': 'Close'},
                        'width': '10%'},
                        {'if': {'column_id': 'Volume'},
                        'width': '10%'},
                        {'if': {'column_id': 'Stock Splits'},
                        'width': '5%'},
                        {'if': {'column_id': 'Dividends'},
                        'width': '5%'}
                        ]




fig = px.line(get_prices("VTR")["Close"])


app.layout=html.Div([
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
                                        columns=columns,
                                        data=df.to_dict('records'),
                                        page_size=10,
                                        style_cell_conditional=style_cell_conditional
                                        ),
                                        style = {
                                        "width":"800px"
                                        }
                            ),
                    dcc.Graph(id='prices-chart',figure=fig),
                    dcc.Slider(
                                id='year-slider',
                                min=1,
                                max=7,
                                value=1,
                                marks={
                                        1: {'label': '5y'},   
                                        2: {'label': '3y'},
                                        3: {'label': '1y'}, 
                                        4: {'label': '6m'},
                                        4: {'label': '3m'},
                                        5: {'label': '1m'},
                                        6: {'label': '7d'},
                                        7: {'label': '1d'},
                                    },
                                step=1,

                            )
                    
])
]
)

@app.callback([
    Output(component_id='table-title', component_property='children'),
    Output('table', 'data'),
    Output('prices-chart', 'figure')],
    Input(component_id='year-slider', component_property='value')
)
def update_data(selected_stock):
    ctx = dash.callback_context

    if not ctx.triggered:
       filtered_df = get_prices(selected_stock)
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    #filtered_df = get_prices(selected_stock)
    fig = px.line(filtered_df["Close"])
    fig.update_layout(transition_duration=500)

    return 'Prices of: {}'.format(selected_stock), filtered_df.to_dict('records') ,fig


@app.callback(
    Output('prices-chart', 'figure'),
    Input(component_id='year-slider', component_property='value')
)
def update_chart(time_frame):

    filtered_df = df.last(time_frame)
    fig = px.line(filtered_df["Close"])

    return fig




if __name__=='__main__':
    app.run_server(debug=True)



