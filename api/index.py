from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

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

@app.route('/tc')
def tc():
    return render_template('tc.html')
    
@app.route('/sc')
def sc():
    name = 'John Doe'
    
    # Send a GET request to the URL
    url = 'http://www.weather.com.cn/weather1d/101020100.shtml'
    response = requests.get(url)
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the element containing the temperature value
    temperature_element = soup.find(class_='tem')
    
    # Extract the temperature value from the element
    temperature = temperature_element.text.strip()

    return render_template('sc.html', name=temperature)
