from dash.dependencies import Input, Output, State
import dash

def register_callbacks(app: dash.Dash):
    @app.callback(
        Output('pressed-buttons-store', 'data'),
        [Input({'type': 'button', 'index': all}, 'n_clicks')],
        [State('pressed-buttons-store', 'data')]
    )
    def update_pressed_buttons(n_clicks, pressed_buttons):
        ctx = dash.callback_context
        if not ctx.triggered:
            button_id = 'No buttons yet'
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id not in pressed_buttons:
            pressed_buttons.append(button_id)
        return pressed_buttons
