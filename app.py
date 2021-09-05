import dash
from constants import EXTERNAL_STYLESHEETS

app= dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)
server = app.server