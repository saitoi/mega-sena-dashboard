import pandas as pd
import plotly.graph_objects as go

# Carregando os dados
df_sena = pd.read_csv('Resultados_sena.csv')

# Inicializando listas para armazenar os dados do scatter plot
x_positions = []
y_numbers = []
sizes = []  # Usaremos o tamanho do marcador para representar a frequência

# Contando a frequência de cada número em cada posição e preenchendo as listas
for dezena in range(1, 7):
    for num in range(1, 51):
        freq = df_sena[df_sena[f'{dezena}ª'] == num].shape[0]
        if freq > 0:  # Considerando apenas frequências positivas para simplificar
            x_positions.append(f'{dezena}ª')
            y_numbers.append(num)
            sizes.append(freq)

# Criando o scatter plot
fig = go.Figure(data=go.Scatter(
    x=x_positions,
    y=y_numbers,
    mode='markers',
    marker=dict(
        size=[s for s in sizes],  # Ajustando o tamanho dos marcadores com base na frequência
        color=sizes,  # Usando a frequência também para definir a cor
        colorscale='Greens',  # Escala de cores para os marcadores
        showscale=True  # Mostra a barra de cores indicando a relação entre cor e frequência
    ),
    text=sizes,  # Mostrar a frequência como texto ao passar o mouse (opcional)
))

# Atualizando o layout do gráfico
fig.update_layout(
    title='Frequência de Números Sorteados por Posição na Mega Sena',
    xaxis_title='Posição da Dezena',
    yaxis_title='Número Sorteado',
    yaxis=dict(autorange='reversed', dtick=1),  # Garantindo que todos os números sejam mostrados
)

fig.show()
