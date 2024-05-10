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
    html.Img(src="assets/result.png", style={'display': 'block', 'margin': 'auto'})
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
