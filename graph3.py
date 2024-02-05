import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Load your CSV data
df_sena = pd.read_csv('Resultados_sena.csv')

# Initialize a dictionary to count frequencies for each position
dezenas = [{} for _ in range(6)]

# Count the frequencies of numbers in each position
for index in range(6):
    for value in df_sena[f'{index+1}ª']:
        dezenas[index][value] = dezenas[index].get(value, 0) + 1

data_for_heatmap = np.zeros((60, 6))
top_frequencies = []

for col_index, dezena in enumerate(dezenas):
    max_frequency = 0
    top_number = 0
    for key, value in dezena.items():
        row_index = key - 1  # Adjust for 0-based indexing
        data_for_heatmap[row_index, col_index] = value
        if value > max_frequency:
            max_frequency = value
            top_number = row_index
    top_frequencies.append(top_number + 1)  # Store the number with the highest frequency

fig = go.Figure(data=go.Contour(
    z=data_for_heatmap,
    x=[f'{i}ª' for i in range(1, 7)],
    y=[str(i) for i in range(1, 61)],
    hoverongaps=False,
    colorbar=dict(title='Frequency'),
    colorscale = [
        [0.0, 'black'],        # start with black
        [0.25, 'darkgreen'],   # transition to dark green
        [0.5, 'green'],        # then to green
        [0.75, 'lightgreen'],  # then to light green
        [1.0, 'white']         # and end with white
    ]
))

fig.update_layout(
    width=400,
    height=500,
    yaxis=dict(tickvals=[i for i in range(0, 61, 10)], ticktext=[str(i) for i in range(0, 61, 10)]),
    yaxis_nticks=7,
    margin=dict(l=20, r=0, t=20, b=0),
    plot_bgcolor='white',
    images=[
        dict(
            source="assets/bilhete-mega-sena.jpg",  # Replace with the URL or local file path to your image
            xref="paper",
            yref="paper",
            x=0,
            y=1,
            sizex=1,
            sizey=1,
            opacity=0.5,  # Adjust the opacity of the background image
            layer="below",  # Place the image below the plot
        )
    ],
)

fig.add_trace(go.Scatter(x=[f'{i}ª' for i in range(1, 7)], y=top_frequencies, mode='lines+markers', marker=dict(color='gold'), line=dict(color='gold')))

print(fig.to_html(full_html=False, include_plotlyjs='cdn'))

fig.show()
