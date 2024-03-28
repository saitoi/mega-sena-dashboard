from flask import Flask, render_template, request

server = Flask(__name__)

@server.route('/')
def dashboard():
    pressed_buttons = {}
    
    return render_template('index.html')
