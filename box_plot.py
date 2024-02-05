import pandas as pd
import plotly.graph_objects as go

# Load your DataFrame
df_sena = pd.read_csv('Resultados_sena.csv')

# Define greenish colors for the box plots
greenish_colors = ['#e5f5e0', '#a1d99b', '#74c476', '#41ab5d', '#238b45', '#005a32']

fig = go.Figure()

mean_values = [df_sena[f'{i+1}ª'].mean() for i in range(6)]  # Pre-calculate mean values

for i, column in enumerate([f'{i+1}ª' for i in range(6)]):
    data = df_sena[column]

    # Add the box plot for each dataset
    fig.add_trace(go.Box(
        x=data,
        name=column,
        marker_color='darkgreen',
        boxpoints=False,  # Hides the outliers/fences
    ))

# Add a single scatter trace for all means to appear once in the legend
fig.add_trace(go.Scatter(
    x=mean_values,  # X positions for all mean values
    y=[f'{i+1}ª' for i in range(6)],  # Y positions based on the box plot's positions
    mode='markers',
    marker_symbol='circle-x',
    marker_size=10,
    marker_color='gold',  # Gold color for the mean
    name='Média',  # This ensures only one legend item for "Média"
))

fig.update_layout(
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,  # Pushes the legend above the graph
        xanchor='right',
        x=1
    ),
    # xaxis=dict(title='Sorteados'),
    yaxis=dict(title='Dezena'),
    plot_bgcolor='white',
    height=600,
    width=600
)

print(fig.to_html(full_html=False, include_plotlyjs='cdn'))

# Show the figure
fig.show()
