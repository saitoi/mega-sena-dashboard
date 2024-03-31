import dash_table
import pandas as pd
from .histogram_kde import df

numeros_sorteados = df.loc[:, '1ª':'6ª']

frequencia = numeros_sorteados.apply(pd.Series.value_counts).sum(axis=1).astype(int).sort_values(ascending=False)

df_frequencia = frequencia.reset_index().rename(columns={'index': 'Dezena', 0: 'Frequencia'}).sort_values(by='Frequencia', ascending=False)

tabela_frequencia = dash_table.DataTable(
    data=df_frequencia.to_dict('records'),
    columns=[{'name': col, 'id': col} for col in df_frequencia.columns],
    style_table={'height': '300px', 'overflowY': 'auto'},
    style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
    style_cell={'textAlign': 'center'},
)