from flask import Flask, render_template
from dash import Dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", dash_url="/dash/")

# Initialize the Dash app
dash_app = Dash(__name__, server=app, url_base_pathname='/dash/')

# Sample data for graphs
df1 = px.data.iris()  # Sample dataset
df2 = px.data.gapminder().query("country=='Canada'")  # Another sample dataset

# Dash app layout with multiple graphs
dash_app.layout = html.Div([
    html.H3("Dash Graphs:"),
    dcc.Graph(id='graph1',
              figure=px.scatter(df1, x='sepal_width', y='sepal_length',
                                color='species', title="Iris Dataset")),
    dcc.Graph(id='graph2',
              figure=px.line(df2, x='year', y='lifeExp', title="Life Expectancy in Canada"))
])

if __name__ == '__main__':
    app.run(debug=True)
