from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getFact')
def getFact():
    url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
    headers = {'Accept': 'application/json'}
    fact = requests.get(url, headers=headers).json()
    return fact

if __name__ == '__main__':
    app.run(debug=True)
