import pandas as pd
import plotly.graph_objects as go

# Extraindo os dados
df_sena = pd.read_csv('Resultados_sena.csv')

df_sena['Ano'] = df_sena['Data'].apply(lambda x: x.split('/')[2])

df_sena['Premio_sena'] = df_sena['Premio_sena'].astype(str).str.replace(',', '')
df_sena['Premio_sena'] = pd.to_numeric(df_sena['Premio_sena'], errors='coerce')

media_premio_anos = df_sena.groupby('Ano')['Premio_sena'].mean()
ganhadores_anos = df_sena.groupby('Ano')['Ganhadores'].sum()

fig = go.Figure(
    data=go.Bar(
        x=media_premio_anos.index,
        y=media_premio_anos.values,
        name='Média dos Prêmios',
        marker=dict(color='green')
    )
)

fig.add_trace(
    go.Scatter(
        x=ganhadores_anos.index,
        y=ganhadores_anos.values,
        name='Número de Ganhadores',
        mode='lines+markers',
        line=dict(color='gold'),
        marker=dict(color='gold'),
        yaxis='y2'
    )
)

fig.update_layout(
    width=800,
    height=600,
    yaxis2=dict(
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

print(fig.to_html(full_html=False, include_plotlyjs='cdn'))

fig.show()
