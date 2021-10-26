import dash_html_components as html
from dash import dcc
import plotly.express as px
from utils.yahoo import TickerData

df = TickerData("VTR").get_earnings()
chart = px.bar(data_frame=df, x = df.index,y = ['Earnings','Revenue'], barmode='group',labels=['x','y'])

bar_chart = html.Div(
                        dcc.Graph(id = 'earnings-chart', figure = chart)
)