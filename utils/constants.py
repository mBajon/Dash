MARKS = {
    1: {"label": "5y"},
    2: {"label": "3y"},
    3: {"label": "1y"},
    4: {"label": "6m"},
    5: {"label": "3m"},
    6: {"label": "1m"},
    7: {"label": "7d"},
}

TIME_FRAMES = {1: "5Y", 2: "3Y", 3: "6M", 4: "3M", 5: "1M", 6: "7D"}

FIELD_MAP = {
    "fiftyTwoWeekHigh": "52 Week High",
    "fiftyTwoWeekLow": "52 Week Low",
    "fiftyDayAverage": "50 Day Average",
    "regularMarketVolume": "Regular Market Volume",
    "averageDailyVolume10Day": "Average Daily Volumne in 10 days",
    "longName": "Name",
    "country": "Country",
    "exchange": "Exchange",
    "sector": "Sector",
    "industry": "Industry",
    "fullTimeEmployees": "Full Time Employees",
    "marketCap": "Market Capitalization",
}
TRADING_DATA = [
    "fiftyTwoWeekHigh",
    "fiftyTwoWeekLow",
    "fiftyDayAverage",
    "regularMarketVolume",
    "averageDailyVolume10Day",
]
GENERAL_INFO = [
    "longName",
    "country",
    "exchange",
    "sector",
    "industry",
    "fullTimeEmployees",
    "marketCap",
]

FORMAT_MAP = {
    "fiftyTwoWeekHigh": "Currency",
    "fiftyTwoWeekLow": "Currency",
    "fiftyDayAverage": "Currency",
    "regularMarketVolume": "Number",
    "averageDailyVolume10Day": "Number",
    "longName": "String",
    "country": "String",
    "exchange": "String",
    "sector": "String",
    "industry": "String",
    "fullTimeEmployees": "Number",
    "marketCap": "Currency",
}

EXPECTED_RESULTS = {'7d': '0.00%', '1m': '0.00%', '3m': '0.00%', '6m': '0.00%', '1y': '0.00%', '3y': '0.00%', '5y': '0.00%'}