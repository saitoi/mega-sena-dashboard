import dash
from dash import dcc, html
import plotly.graph_objs as go

# Suponha que tenhamos os seguintes dados para nosso gráfico:
eixo_x = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul']  # Por exemplo, os meses
barras_y = [20, 30, 40, 25, 50, 60, 55]  # Dados para as barras
linha_y = [15, 25, 35, 20, 45, 55, 50]  # Dados para a linha

# Criar a figura com um gráfico de barras e um gráfico de linha
figura = go.Figure(data=[
    go.Bar(x=eixo_x, y=barras_y, name='Média das Premiações'),  # Gráfico de barras
    go.Scatter(x=eixo_x, y=linha_y, name='Número de Ganhadores', mode='lines+markers')  # Gráfico de linha
])

# Configuração do layout do gráfico
figura.update_layout(
    title='Premiações vs. Número de Ganhadores',
    xaxis_title='Mês',
    yaxis_title='Valor',
    legend_title='Legenda',
    template='plotly_dark'  # Ou outro tema de sua escolha
)

app = dash.Dash(__name__)

# Definir o layout da aplicação Dash para incluir o gráfico Plotly
app.layout = html.Div([
    dcc.Graph(
        id='example-graph',
        figure=figura
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
