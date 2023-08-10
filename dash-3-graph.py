import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import random

# Sample countries and synthetic data
countries = ['USA', 'India', 'China', 'Brazil', 'Russia', 'Germany', 'UK', 'France', 'Italy', 'Spain']
birth_rates = [random.randint(10, 20) for _ in countries]
death_rates = [random.randint(5, 10) for _ in countries]

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='live-graph'),
    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
    )
])

@app.callback(Output('live-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph(n):
    # Update the birth and death rates with synthetic variations for the example
    global birth_rates, death_rates
    birth_rates = [rate + random.choice([-0.5, 0.5]) for rate in birth_rates]
    death_rates = [rate + random.choice([-0.5, 0.5]) for rate in death_rates]

    trace1 = go.Bar(x=countries, y=birth_rates, name='Births', marker_color='blue')
    trace2 = go.Bar(x=countries, y=death_rates, name='Deaths', marker_color='red')

    layout = go.Layout(title='Live Births and Deaths of 10 countries', barmode='group')
    return {'data': [trace1, trace2], 'layout': layout}

if __name__ == '__main__':
    app.run_server(debug=True)
