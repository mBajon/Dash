import dash
from dash.dependencies import Input, Output,State, MATCH
import plotly.express as px
from app import app
from utils.yahoo import TickerData
import plotly.express as px


@app.callback(
    Output('dynamic-charts-container', 'children'),
    Input(component_id='stock-name-dropdown', component_property='value'),
    State('dynamic-charts-container', 'children')
    )
def display_earnings_chart(selected_stock):
    df = TickerData("VTR").get_earnings()
    df_r = TickerData("VTR").get_recommendations()
    chart = px.bar(data_frame=df, x = df.index,y = ['Earnings','Revenue'], barmode='group',labels=['x','y'])
    recomendations_chart = px.bar(data_frame=df_r, x = 'To Grade',y = 'counts', barmode='group',labels=['x','y'])
    
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
