from dash import Dash, html
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World'),
    html.Button('Click Me', id='example-button'),  # Add a button
    html.Div(id='button-clicks')  # Placeholder to display click count
])

# Callback to update the button-clicks Div based on button clicks
@app.callback(
    Output('button-clicks', 'children'),
    Input('example-button', 'n_clicks')
)
def update_output(n_clicks):
    if n_clicks is None:
        return 'Button has not been clicked yet'
    else:
        return f'Button has been clicked {n_clicks} times'

if __name__ == '__main__':
    app.run_server(debug=True)
