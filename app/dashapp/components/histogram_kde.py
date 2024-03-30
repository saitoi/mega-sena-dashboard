import pandas as pd
import plotly.graph_objs as go


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

histograma_kde = go.Figure().add_trace(bar_trace).add_trace(scatter_trace)

histograma_kde.update_layout(
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