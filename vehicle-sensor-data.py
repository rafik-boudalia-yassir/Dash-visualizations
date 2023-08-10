import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Generate dataset
time_points = pd.date_range(start="2023-08-08 08:00:00", end="2023-08-08 08:10:00", freq='10S')
speed = np.random.randint(0, 120, size=len(time_points))  # random speeds between 0 and 120 km/h

# Create dataframe
df = pd.DataFrame({
    'time': time_points,
    'speed': speed
})

# Create a Dash application
app = dash.Dash(__name__)

# Design the layout of the app
app.layout = html.Div([
    html.H1("Vehicle Sensor Data Visualization"),
    dcc.Graph(id="vehicle-speed-graph"),
    dcc.Interval(id='interval-component', interval=10*1000, n_intervals=0)  # update every 10 seconds
])

# Define callback to update graph
@app.callback(
    Output("vehicle-speed-graph", "figure"),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    trace = go.Scatter(x=df['time'], y=df['speed'], mode='lines+markers')
    layout = go.Layout(title="Vehicle Speed Over Time", xaxis=dict(title="Time"), yaxis=dict(title="Speed (km/h)"))
    return {"data": [trace], "layout": layout}

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
