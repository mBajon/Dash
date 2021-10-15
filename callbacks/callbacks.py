import dash
from dash.dependencies import Input, Output
import plotly.express as px
from app import app
from layouts.layouts import df
from layouts.table_layouts import generate_table
from utils.yahoo import TickerData

@app.callback(
    Output('prices-chart', 'figure'),
    Input(component_id='stock-name-dropdown', component_property='value'),
    Input(component_id='year-slider', component_property='value')
    
)
def update_data(selected_stock, time_frame):

    time_frames= {
        1:'5Y',
        2:'3Y',
        3:'6M',
        4:'3M',
        5:'1M',
        6:'7D'
    }
    
    filtered_df = df
    fig = px.line(filtered_df["Close"])
    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id']=='stock-name-dropdown.value' :
        filtered_df = TickerData(selected_stock).get_prices().last(time_frames[time_frame])
        fig = px.line(filtered_df["Close"])

    else:
        if ctx.triggered[0]['prop_id']=='year-slider.value':
            filtered_df = df.last(time_frames[time_frame])
            fig = px.line(filtered_df["Close"])
        
    return fig




    
