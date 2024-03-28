from dash import Dash
from flask import Flask
from .layout import create_layout
from .callbacks import register_callbacks

def create_dash_application(flask_app: Flask) -> Dash:
    """
    Creates and configures the dash application to run in the Flask server
    
    Parameters:
    - flask_app: The Flask application instance.
    
    Returns:
    - dash_app: The Dash application instance.
    """
    
    dash_app = Dash(__name__, server=flask_app, url_base_pathname='/dash/', suppress_callback_exceptions=True)
    
    dash_app.layout = create_layout()
    
    register_callbacks(dash_app)
    
    return dash_app
