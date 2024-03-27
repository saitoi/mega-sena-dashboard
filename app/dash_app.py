import dash
import dash_table
from dash import html
import pandas as pd


def criar_botoes_ficha(tipo: str, inicio: int, fim: int, intervalo: int=1) -> list[html.Button]:
    """
    Cria uma lista de elementos html.Button numerados.
    
    :param tipo: Uma string que define o tipo ou categoria dos botões.
    :param inicio: Um inteiro que define o número inicial da sequência de botões.
    :param fim: Um inteiro que define o número final da sequência de botões.
    :return: Uma lista contendo os botões criados.
    """
    return [html.Button(str(i), id=f'button-{tipo}-{i}') for i in range(inicio, fim+1, intervalo)]


df = pd.read_csv('/data/sorteios-principal.csv')

app = dash.Dash(__name__)

ficha = html.Div(
    # "Navbar"
    html.Div(
        
    ),
    
    # Conteúdo Central
    html.Div(
        html.Div(
            criar_botoes_ficha('dezena_1', 1, 61),          # Tabela 1
            
            html.P('Para anular este jogo marque: '),
            html.Button(),
            
            criar_botoes_ficha('dezena_2', 1, 61),          # Tabela 2
            
            html.P('Para anular este jogo marque: '),
            html.Button(),
            
            criar_botoes_ficha('alternativa', 6, 16),       # Número de Alternativas
            criar_botoes_ficha('surpresinha', 1, 8),        # Surpresinha
            criar_botoes_ficha('teimosinha', 2, 8, 2),      # Teimosinha
        )
    )
)

# tabela_fixa

app.layout = html.Div([
    # Ficha Mega-Sena
    
    
    # Gráfico Principal
    html.Div(),
    
    # Gráfico de Sorteios Correspondidos
    html.Div(),
    
    # Tabela Fixa
    html.Div()
])