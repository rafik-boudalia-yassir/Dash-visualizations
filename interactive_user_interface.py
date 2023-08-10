import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Input(id='input', value='Enter Something', type='text'),
    html.Div(id='output')

    ])

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input',component_property='value')])
def update_value(input_data):
    try:
        return str(float(input_data)**2)
    except:
        return "Error: Make sure that you put a float values because it is mathematical operation"

if __name__ == '__main__':
    app.run_server(debug=True)
