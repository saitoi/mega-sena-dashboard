import numpy as np
import plotly.graph_objects as go

# Let's say we have some original heatmap data like this:
original_data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# We want to divide each block into 10x10 smaller blocks
# So we create a new array with the increased resolution
resolution_factor = 10
new_shape = (original_data.shape[0] * resolution_factor,
             original_data.shape[1] * resolution_factor)
high_res_data = np.zeros(new_shape)

# Now we populate the high resolution data with the original data values
for i in range(original_data.shape[0]):
    for j in range(original_data.shape[1]):
        high_res_data[i*resolution_factor:(i+1)*resolution_factor,
        j*resolution_factor:(j+1)*resolution_factor] = original_data[i, j]

# Now, 'high_res_data' can be used to create a heatmap that simulates mini heatmaps within each block
fig = go.Figure(data=go.Heatmap(
    z=high_res_data,
    colorscale='Viridis',
    showscale=True
))

# Set plot layout
fig.update_layout(
    title='Heatmap with Mini Blocks',
    xaxis_nticks=original_data.shape[1],
    yaxis_nticks=original_data.shape[0]
)

# Show plot
fig.show()
