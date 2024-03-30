from dash import html, dcc

def criar_botoes_ficha(tipo: str, inicio: int, fim: int, intervalo: int=1) -> list[html.Button]:
    """Creates a list of numbered html.Button elements."""
    return [html.Button(f'[{tipo}]', id=f'button-{tipo}-{i}') for i in range(inicio, fim+1, intervalo)]

def secao_jogo(numero: int) -> html.Div:
    """Creates a section of a game table with buttons and cancellation options."""
    return html.Div([
                html.P(f'Tabela {numero}'),
                criar_botoes_ficha(f'dezena_{numero}', 1, 60),
                html.P('Para anular este jogo marque: '),
                html.Button('[  ]', id=f'anular-{numero}')
            ])

def create_main_content() -> html.Div:
    """Create central content with sections for the game, alternatives, and more."""
    return html.Div([
        secao_jogo(1),  # Tabela 1
        secao_jogo(2),  # Tabela 2
        html.P("Assinale quantos números você está marcando nesse jogo"),
        *criar_botoes_ficha('alternativa', 6, 16),  # Número de Alternativas
        html.P("SURPRESINHA - Aqui o sistema escolhe os números por você. Indique \
                quantas apostas deseja fazer:"),
        *criar_botoes_ficha('surpresinha', 1, 8),  # SURPRESINHA
        html.P("TEIMOSINHA - Escolha em quantos concursos você quer participar com \
                esse mesmo jogo."),
        *criar_botoes_ficha('teimosinha', 2, 8)  # TEIMOSINHA
    ])

def create_layout() -> html.Div:
    """Create.."""
    return html.Div([
        create_main_content(),
        # Falta alguns gráficos
    ])
