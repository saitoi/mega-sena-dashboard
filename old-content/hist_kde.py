import pandas as pd
import plotly.graph_objects as go

# Extraindo os dados
df_sena = pd.read_csv('data/sorteios-secundario.csv')

df_sena['Ano'] = pd.to_datetime(df_sena['Data']).dt.year
df_sena['Premio_sena'] = df_sena['Premio_sena'].str.replace(',', '').astype(float)

media_premio_anos = df_sena.groupby('Ano')['Premio_sena'].mean()
ganhadores_anos = df_sena.groupby('Ano')['Ganhadores'].sum()

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

# Initialize the figure and add the traces
hist = go.Figure().add_trace(bar_trace).add_trace(scatter_trace)

# Update the layout in one go
hist.update_layout(
    width=1000,
    height=500,
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

print(hist.to_html(full_html=False, include_plotlyjs='cdn'))

hist.show()
