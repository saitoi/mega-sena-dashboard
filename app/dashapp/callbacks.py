from dash.dependencies import Input, Output, State, ALL
from dash import callback_context
import dash_table
import pandas as pd

def dezena_frequency_table(selected_buttons: set) -> None:
    df = pd.read_csv('/../../data/sorteios-secundario.csv')
    
    
    
    pass

def register_callbacks(app):
    @app.callback(
        Output('pressed-buttons-store', 'data'),
        Input({'type': 'button', 'index': ALL}, 'n_clicks'),
        State('pressed-buttons-store', 'data')
    )
    def update_pressed_buttons(n_clicks, pressed_buttons_data):
        if pressed_buttons_data is None:
            pressed_buttons_data = {}

        if callback_context.triggered:
            button_id = callback_context.triggered[0]['prop_id'].split('.')[0]

            if button_id in pressed_buttons_data:
                pressed_buttons_data.remove(button_id)
            else:
                pressed_buttons_data.append(button_id)

        return pressed_buttons_data

    @app.callback(
        Output('output-area', 'children'),  # Atualiza o conteúdo desta Div com o resultado do cálculo
        Input('pressed-buttons-store', 'data')  # Ativado pelos dados atualizados em 'pressed-buttons-store'
    )
    def proccessed_data_to_table(pressed_buttons_data):
        """
        Button general format:
        button_id = [
            table_id,
            type,
            number
        ]
        """
        button_types_count = {
            'surpresinha': 0,
            'dezena': 0,
            'teimosinha': 0
        }
        
        chosen_buttons = {
            'table1': {},
            'table2': {}
        }
        
        # Defining the type of buttons
        for table, type, number in pressed_buttons_data:
            button_types_count[type] += 1
            
            key = 'table1' if table == 1 else 'table2'
            chosen_buttons[key].append(number)
            
        if button_types_count['surpresinha'] >= 1:
            # Logica da Surpresinha
            # TODO Função para seleção aleatória dos botões
            pass
        elif 6 <= button_types_count['dezena'] <= 15:
            # TODO Chamar função para gerar gráfico
            pass
        else:
            pass
        