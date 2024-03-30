from dash.dependencies import Input, Output, State, ALL
from dash import callback_context

def register_callbacks(app):
    @app.callback(
        Output('pressed-buttons-store', 'data'),
        Input({'type': 'button', 'index': ALL}, 'n_clicks'),
        State('pressed-buttons-store', 'data')
    )
    def update_pressed_buttons(n_clicks, pressed_buttons_data):
        if pressed_buttons_data is None:
            pressed_buttons_data = []

        if callback_context.triggered:
            button_id = callback_context.triggered[0]['prop_id'].split('.')[0]

            if button_id in pressed_buttons_data:
                pressed_buttons_data.remove(button_id)
            else:
                pressed_buttons_data.append(button_id)

        return pressed_buttons_data

    @app.callback(
        # Suponha que aqui você definiria os Inputs, Outputs e States para o segundo callback
    )
    def calcular_ficha_frequencia():
        pass
        # Sua lógica aqui
