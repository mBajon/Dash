import dash_table.FormatTemplate as FormatTemplate

EXTERNAL_STYLESHEETS = ['https://codepen.io/chriddyp/pen/bWlwgP.css']
COLUMNS = [
            {"name": "Open", "id": "Open", 'type': 'numeric','format': FormatTemplate.money(2)},
            {"name": "High", "id": "High", 'type': 'numeric','format': FormatTemplate.money(2)},
            {"name": "Low", "id": "Low", 'type': 'numeric','format': FormatTemplate.money(2)},
            {"name": "Close", "id": "Close", 'type': 'numeric','format': FormatTemplate.money(2)},
            {"name": "Volume", "id": "Volume", 'type': 'numeric'},
            {"name": "Dividends", "id": "Dividends", 'type': 'numeric','format': FormatTemplate.money(2)},
            {"name": "Stock Splits", "id": "Stock Splits", 'type': 'numeric'}
        ]

STYLE_CELL_CONDITIONAL=[
                        {'if': {'column_id': 'Open'},
                        'width': '10%'},
                        {'if': {'column_id': 'High'},
                        'width': '10%'},
                        {'if': {'column_id': 'Low'},
                        'width': '10%'},
                        {'if': {'column_id': 'Close'},
                        'width': '10%'},
                        {'if': {'column_id': 'Volume'},
                        'width': '10%'},
                        {'if': {'column_id': 'Stock Splits'},
                        'width': '5%'},
                        {'if': {'column_id': 'Dividends'},
                        'width': '5%'}
                        ]
