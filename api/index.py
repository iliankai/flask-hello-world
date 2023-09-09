from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About'

@app.route('/best')
def best():
    return render_template('best.html')

@app.route('/sc')
def sc():
    name = 'John Doe'
    return render_template('sc.html', name=name)
