# Install necessary libraries if you haven't
# pip install dash pandas numpy

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Create some dummy data
np.random.seed(42)
time_series = np.cumsum(np.random.randn(100))

# App layout
app.layout = html.Div([
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    ),
    html.Button('Introduce Change', id='change-button', n_clicks=0)
])

@app.callback(
    Output('live-graph', 'figure'),
    [Input('interval-component', 'n_intervals'),
     Input('change-button', 'n_clicks')]
)
def update_graph(n_intervals, n_clicks):
    global time_series

    # Introduce a sudden change when the button is clicked
    if n_clicks > 0:
        time_series = np.cumsum(np.random.randn(100)) + 20

    # Simulate new data
    new_point = time_series[-1] + np.random.randn(1)[0]
    time_series = np.append(time_series[1:], new_point)

    # Plot the updated data
    fig = {
        'data': [{
            'x': list(range(len(time_series))),
            'y': time_series,
            'type': 'line'
        }],
        'layout': {
            'title': 'Live Data'
        }
    }

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
