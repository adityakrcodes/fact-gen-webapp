from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getFact')
def getFact():
    url = 'http://127.0.0.1:5000/'
    headers = {'Accept': 'application/json'}
    fact = requests.get(url, headers=headers).json()
    print(fact)
    return fact

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5501')
