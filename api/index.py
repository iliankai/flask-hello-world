from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hellooo, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/best')
def index():
    return render_template('best.html')
