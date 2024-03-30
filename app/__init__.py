from flask import Flask
from .dashapp import create_dash_application
from config import Config

def create_app(config_class=Config):
    """
    Creates and configures the Flask application.

    Returns:
        flask_app (Flask): The configured Flask application.
    """
    flask_app = Flask(__name__)
    
    return create_dash_application(flask_app)
