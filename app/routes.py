from flask import render_template, request
from . import app

@app.route('/')
def index():
    dash_url = '/dash'
    return render_template('index.html', dash_url=dash_url)
