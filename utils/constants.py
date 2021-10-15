from dash_table import FormatTemplate
import dash_bootstrap_components as dbc

EXTERNAL_STYLESHEETS = [dbc.themes.BOOTSTRAP]
FIELD_MAP = {
    'fiftyTwoWeekHigh':'52 Week High',
    'fiftyTwoWeekLow':'52 Week Low',
    'fiftyDayAverage':'50 Day Average',
    'regularMarketVolume':'Regular Market Volume',
    'averageDailyVolume10Day':'Average Daily Volumne in 10 days',
    'volume24Hr':'Volume',
    'longName':'Name',
    'country':'Country',
    'exchange':'Exchange',
    'sector':'Sector',
    'industry':'Industry',
    'fullTimeEmployees':'Full Time Employees',
    'marketCap':'Market Capitalization',
}
TRADING_DATA=['fiftyTwoWeekHigh','fiftyTwoWeekLow','fiftyDayAverage', 'regularMarketVolume','averageDailyVolume10Day', 'volume24Hr']
GENERAL_INFO=['longName','country','exchange', 'sector','industry', 'fullTimeEmployees', 'marketCap']

