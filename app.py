from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
import numpy as np
import utils

# Sample boolean array
bool_matrix = np.random.choice([True, False], size=(5, 10))  # Example random boolean matrix
utils.save_boolean_matrix(bool_matrix, "assets/result")

# Create the Plotly Dash app
app = Dash(__name__)

server = app.server

# Define the layout of the app
app.layout = html.Div([
    html.H1("Instrument Classification Results", style={'text-align': 'center'}),
    html.Img(id="boolean-matrix-img", src="assets/result.png", style={'display': 'block', 'margin': 'auto'}),
    dcc.Interval(id='update-interval', interval=5*1000, n_intervals=0),
    html.H1("Counter:"),
    html.Div(id='counter-output'),
])

@app.callback(
    Output('boolean-matrix-img', 'src'),
    [Input('update-interval', 'n_intervals')]
)

def update_graph(n_intervals):
    # Call the function to update the boolean matrix every 5 seconds
    utils.save_boolean_matrix(np.random.choice([True, False], size=(5, 10)), "assets/result.png")
    # Return the updated image source
    return "assets/result.png"

@app.callback(
    Output('counter-output', 'children'),
    [Input('update-interval', 'n_intervals')]
)

def update_counter(n_intervals):
    return f"Interval count: {n_intervals}"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
