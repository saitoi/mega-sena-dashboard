import os

class Config:
    FLASK_ENDPOINT = os.environ.get('FLASK_ENDPOINT') or ''
    