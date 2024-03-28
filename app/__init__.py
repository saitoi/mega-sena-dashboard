from flask import Flask
from .dashapp import create_dash_application

def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        flask_app (Flask): The configured Flask application.
    """
    flask_app = Flask(__name__)
    
    create_dash_application(flask_app)
    
    return flask_app