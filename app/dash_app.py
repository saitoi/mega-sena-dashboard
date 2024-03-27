import dash
import dash_table
from dash import html, dcc, Input, Output, State
from dash.dependencies import ALL
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash(__name__)

# ***************** FICHA *****************

def criar_botoes_ficha(tipo: str, inicio: int, fim: int, intervalo: int=1) -> list[html.Button]:
    """
    Cria uma lista de elementos html.Button numerados.
    
    :param tipo: Uma string que define o tipo ou categoria dos botões.
    :param inicio: Um inteiro que define o número inicial da sequência de botões.
    :param fim: Um inteiro que define o número final da sequência de botões.
    :return: Uma lista contendo os botões criados.
    """
    return [html.Button(f'[{tipo}]', id=f'button-{tipo}-{i}') for i in range(inicio, fim+1, intervalo)]


def secao_jogo(numero: int) -> list:
    """Cria a seção de uma tabela de jogo com botões e opções de anulação."""
    return  html.Div([
                html.P(f'Tabela {numero}'),
                criar_botoes_ficha(f'dezena_{numero}', 1, 60),
                html.P('Para anular este jogo marque: '),
                html.Button('[  ]', id=f'anular-{numero}')
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
    # "Navbar"
    html.Div(),
    conteudo_central,
    dcc.Store(id='pressed-buttons-store', data=[])
)

@app.callback(
    Output('pressed-buttons-store', 'data'),
    [Input({'type': 'button', 'index': ALL}, 'n_clicks')],
    [State('pressed-buttons-store', 'data')]
)
def update_pressed_buttons(n_clicks, pressed_buttons):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = 'No buttons yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        # The ID is in a string format like '{"type":"button","index":"button-dezena_1-1"}'
        # You might need to parse this string to extract the exact button ID in your desired format

    if button_id not in pressed_buttons:
        pressed_buttons.append(button_id)

    return pressed_buttons

# ***************** TABELA DE DEZENAS SELECIONADAS *****************



# ***************** HISTOGRAMA COM KDE *****************

df = pd.read_csv('data/sorteios-secundario.csv')

df['Ano'] = pd.to_datetime(df['Data']).dt.year
df['Premio_sena'] = df['Premio_sena'].str.replace(',', '').astype(float)

media_premio_anos = df.groupby('Ano')['Premio_sena'].mean()
ganhadores_anos = df.groupby('Ano')['Ganhadores'].sum()

cor_marcador = 'gold'
cor_linha = 'gold'
cor_barra = 'green'

bar_trace = go.Bar(
    x=media_premio_anos.index,
    y=media_premio_anos.values,
    name='Média dos Prêmios',
    marker=dict(color=cor_barra)
)

scatter_trace = go.Scatter(
    x=ganhadores_anos.index,
    y=ganhadores_anos.values,
    name='Número de Ganhadores',
    mode='lines+markers',
    line=dict(color=cor_linha),
    marker=dict(color=cor_marcador),
    yaxis='y2'
)

hist = go.Figure().add_trace(bar_trace).add_trace(scatter_trace)

hist.update_layout(
    width=1000,
    height=400,
    yaxis=dict(title='Média dos Prêmios'),  # Left Y-axis title
    yaxis2=dict(
        title='Número de Ganhadores',  # Right Y-axis title
        overlaying='y',
        side='right'
    ),
    plot_bgcolor='white',
    paper_bgcolor='white',
    legend=dict(
        orientation="h",
        x=0.5,
        y=1.1,
        xanchor="center",
        yanchor="bottom"
    )
)

# ***************** TABELA ESTÁTICA DE MAIORES VALORES *****************

numeros_sorteados = df.loc[:, '1ª':'6ª']

frequencia = numeros_sorteados.apply(pd.Series.value_counts).sum(axis=1).astype(int).sort_values(ascending=False)

df_frequencia = frequencia.reset_index().rename(columns={'index': 'Dezena', 0: 'Frequencia'}).sort_values(by='Frequencia', ascending=False)

app.layout = html.Div([
    # Ficha Mega-Sena
    ficha,    
    
    # Histograma com KDE
    
    
    # Gráfico de Sorteios Correspondidos
    html.Div(),
    
    # Tabela Fixa
    html.Div()
])