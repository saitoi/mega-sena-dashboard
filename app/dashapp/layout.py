from dash import html, dcc
from components import histograma_kde, tabela_frequencia

def criar_botoes_ficha(tipo: str, tabela: int, inicio: int, fim: int, intervalo: int=1) -> list[html.Button]:
    """Creates a list of numbered html.Button elements."""
    return [
        html.Button(
            children=[
                "[",
                html.Span(f'{i:02d}', className='number'),
                "]"
            ],
            id=f'{tabela}-{tipo}-{i}',
            className='dash_buttons'
        ) for i in range(inicio, fim + 1, intervalo)
    ]

def secao_jogo(numero: int) -> html.Div:
    """Creates a section of a game table with buttons and cancellation options."""
    return html.Div([
                *criar_botoes_ficha(f'dezena', numero, 1, 60),
            ], className='tabela')

def create_main_content() -> html.Div:
    """Create central content with sections for the game, alternatives, and more."""
    return html.Div([
    secao_jogo(1),  # Tabela 1
    secao_jogo(2),  # Tabela 2
    html.P("SURPRESINHA - Aqui o sistema escolhe os números por você. Indique \
        quantas apostas deseja fazer:"),
    *criar_botoes_ficha('surpresinha', 0, 1, 8),  # SURPRESINHA
    html.P("TEIMOSINHA - Escolha em quantos concursos você quer participar com \
        esse mesmo jogo."),
    *criar_botoes_ficha('teimosinha', 0, 2, 8),  # TEIMOSINHA
    ], className='ficha-container')

def create_layout() -> html.Div:
    """Create.."""
    return html.Div([
        # Ficha
        create_main_content(),
        dcc.Graph(figure=histograma_kde),
        html.Div(id='output-area'),
        tabela_frequencia,
    ])
