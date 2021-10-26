import callbacks.callbacks
import callbacks.table_callbacks
import callbacks.bar_chart_callbacks
from layouts.layouts import layout
from app import app

app.layout=layout

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
