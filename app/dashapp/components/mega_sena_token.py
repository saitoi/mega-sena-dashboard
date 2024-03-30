from dash import html, dcc, Input, Output, State, callback_context
from dash.dependencies import ALL
import dash_table

def criar_botoes_ficha(tipo: str, inicio: int, fim: int, intervalo: int=1) -> list[html.Button]:
    """
    Cria uma lista de elementos html.Button numerados.
    
    :param tipo: Uma string que define o tipo ou categoria dos botões.
    :param inicio: Um inteiro que define o número inicial da sequência de botões.
    :param fim: Um inteiro que define o número final da sequência de botões.
    :return: Uma lista contendo os botões criados.
    """
    return [html.Button(f'[{i}]',
                        id=f'{tipo}-{i}',
                        className='dash-buttons') for i in range(inicio, fim+1, intervalo)]


def secao_jogo(numero: int) -> list:
    """Cria a seção de uma tabela de jogo com botões e opções de anulação."""
    return  html.Div([
                html.P(f'Tabela {numero}'),
                criar_botoes_ficha(f'dezena_{numero}', 1, 60),
                html.P('Para anular este jogo marque: '),
                html.Button('[  ]', id=f'anular-{numero}', className='dash-buttons'),
            ])
    

conteudo_central = html.Div([
    secao_jogo(1),                                                              # Tabela 1
    secao_jogo(2),                                                              # Tabela 2
    html.P("Assinale quantos números você está marcando nesse jogo"),
    *criar_botoes_ficha('alternativa', 6, 16),                                   # Número de Alternativas
    html.P("SURPRESINHA - Aqui o sistema escolhe os números por você. Indique \
           quantas apostas deseja fazer:"),
    *criar_botoes_ficha('surpresinha', 1, 8),                                    # SURPRESINHA
    html.P("TEIMOSINHA - Escolha em quantos concursos você quer participar com \
           esse mesmo jogo."),
    *criar_botoes_ficha('teimosinha', 2, 8)                                      # TEIMOSINHA
])

ficha = html.Div(
    # TODO Adicionar topbar da ficha
    html.Div(),
    conteudo_central,
    dcc.Store(id='pressed-buttons-store', data=[])
)

# ***************** CALLBACKS IN "callbacks.py" *****************


# ***************** TABELA CORRESPONDENTE *****************

@app.callback(

)
def calcular_ficha_frequencia() -> None:
    
    pass


df_correspondencia = 

chosen_token_table = dash_table.DataTable(
    data=
)