import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot  # This import may not be needed for your use case

df = pd.read_csv('sorteios.csv')

df['Ano'] = df['Data Sorteio'].apply(lambda x: x.split('/')[2])

qtd_anos = df['Ano'].nunique()

# Gráfico 1: Histograma contendo
fig = px.histogram(df, x='Ano', nbins=qtd_anos,
                   histnorm='probability density',
                   title='Histogram with KDE',
                   labels={'Ano': 'Ano', 'y': 'Densidade'},
                   color='Ano')  # Ensure 'Ano' column exists for color coding; remove if not needed

fig.update_layout(xaxis_title='Ano', yaxis_title='Densidade')
fig.show()
