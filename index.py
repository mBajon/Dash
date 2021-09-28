import callbacks.callbacks
from layouts.layouts import layout
from app import app

app.layout=layout

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)



