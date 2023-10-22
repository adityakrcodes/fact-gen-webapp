from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', )

@app.route('/gen')
def gen():
    print("Hello")
    return {"result": "success"}

if __name__ == '__main__':
    app.run(debug=True)
