import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()

app.layout = html.Div(style={'backgroundColor': 'pink'}, children=[
    html.H1(
        children='Hello Tommy!',
        style={
            'textAlign': 'center',
            'color': 'rebeccapurple'
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)