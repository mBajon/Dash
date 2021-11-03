import dash
from dash.dependencies import Input, Output
import plotly.express as px
from app import app
from layouts.layouts import df
from layouts.table_layouts import generate_table
from utils.yahoo import TickerData
from utils.constants import TIME_FRAMES

@app.callback(
    Output('prices-chart', 'figure'),
    Input(component_id='stock-name-dropdown', component_property='value'),
    Input(component_id='year-slider', component_property='value')
    
)
def display_line_chart(selected_stock, time_frame):
    
    filtered_df = df
    fig = px.line(filtered_df["Close"])
    style_line_chart(fig)
    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id']=='stock-name-dropdown.value' :
        filtered_df = TickerData(selected_stock).get_prices().last(TIME_FRAMES[time_frame])
        fig = px.line(filtered_df["Close"])
        style_line_chart(fig)

    else:
        if ctx.triggered[0]['prop_id']=='year-slider.value':
            filtered_df = df.last(TIME_FRAMES[time_frame])
            fig = px.line(filtered_df["Close"])
            style_line_chart(fig)
        
    return fig

def style_line_chart(fig):
    fig=fig
    fig.update_layout(
                    {
                    'plot_bgcolor': 'rgba(0,0,0,0)',
                    
                    })
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_traces(line_color='rgb(51, 153, 255)')
    fig.yaxis_title='$'

    return fig




    
