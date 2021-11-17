import pandas as pd

def get_tickers()-> DataFrame:
    table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    return df[['Symbol','Security']].copy()

