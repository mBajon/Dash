import dash
from dash.dependencies import Input, Output,State, MATCH
import plotly.express as px
from app import app
from utils.yahoo import TickerData
import plotly.express as px


@app.callback(
    Output('dupa-chart', 'figure'),
    Input(component_id='stock-name-dropdown', component_property='value'),
    )
def display_dropdowns(selected_stock):
    df = TickerData(selected_stock).get_earnings()
    chart = px.bar(data_frame=df, x = df.index,y = ['Earnings','Revenue'], barmode='group')
    chart.update_layout(
                        xaxis={
                        'dtick':1
                        })
    chart.update_xaxes(showgrid=False)
    chart.update_yaxes(showgrid=False)

    return chart
