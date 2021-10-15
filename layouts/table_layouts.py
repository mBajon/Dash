import dash_html_components as html
import dash_bootstrap_components as dbc


def generate_table(data : dict, headers: list)-> None:
    return dbc.Table([
        html.Thead(
            html.Tr([
                html.Th(headers[0], colSpan=2)
                ])
        ),
        html.Tbody([
                html.Tr([html.Td(i), html.Td(data[i])]) for i in data.keys()
                ])],
    className = 'table',
    id={
        'type': 'dynamic-table',
        'index': headers[0]
        }
    )
