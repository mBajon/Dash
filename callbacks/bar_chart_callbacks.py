import dash
from dash.dependencies import Input, Output,State, MATCH
import plotly.express as px
from app import app
from utils.yahoo import TickerData
import plotly.express as px


@app.callback(
    Output('earnings-chart', 'figure'),
    Input(component_id='stock-name-dropdown', component_property='value')
    )
def display_earnings_chart(selected_stock):
    df = TickerData(selected_stock).get_earnings()
    chart = px.bar(data_frame=df, x = df.index,y = ['Earnings','Revenue'], barmode='group',color_discrete_sequence =['rgb(0, 204, 102)','rgb(51, 153, 255)'],title='Earnings & Revenue',)
    chart.update_layout(
                        xaxis={
                        'dtick':1,
                        'showgrid':False
                        },
                        yaxis = {
                            'showgrid':False
                        },
                        title = {'x':0.5,'y':0.88},
                        plot_bgcolor='rgba(0,0,0,0)',
                        yaxis_title=''
                        )

    return chart
