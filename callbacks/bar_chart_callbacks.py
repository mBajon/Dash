
from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
import plotly.express as px
from app import app
from utils.yahoo import TickerData
from layouts.bar_chart_layouts import generate_bar_chart
import plotly.express as px


@app.callback(
    Output('dynamic-charts-container', 'children'),
    Input(component_id='stock-name-dropdown', component_property='value'),
    State('dynamic-charts-container', 'children')
    )
def display_bar_charts(selected_stock : str, children : dict):
    children.clear()
    figure = define_earnings_chart(selected_stock)
    children.append(generate_bar_chart(figure,'earnings-chart'))
    figure = define_recommendations_chart(selected_stock)
    children.append(generate_bar_chart(figure,'recommendations-chart'))

    return children

def style_bar_chart(fig, yaxis_title : str = None) ->dict:
    fig.update_layout(
                        xaxis={
                        'dtick': 1,
                        'showgrid' : False
                        },
                        yaxis = {
                            'showgrid' : False
                        },
                        title = {'x':0.5,'y':0.88},
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor = 'rgba(0,0,0,0)',
                        yaxis_title=yaxis_title
    )

    return fig

def define_earnings_chart(selected_stock : str) -> dict():
    df = TickerData(selected_stock).get_earnings()
    figure = px.bar(data_frame=df,
                    x = df.index,
                    y = ['Earnings','Revenue'],
                    barmode='group',
                    color_discrete_sequence =['rgb(0, 204, 102)','rgb(51, 153, 255)'],
                    title='Earnings & Revenue')
    style_bar_chart(figure,'$')
    
    return figure

def define_recommendations_chart(selected_stock : str) -> dict():
    df = TickerData(selected_stock).get_recommendations()
    figure = px.bar(data_frame=df,
                    x = 'To Grade',
                    y = 'counts',
                    barmode='group',
                    color_discrete_sequence =['rgb(0, 204, 102)'], 
                    labels=['x','y'],title="Analyst's Recommendations")
    style_bar_chart(figure, 'No. of recommendations')
    
    return figure


