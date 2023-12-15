from flask import Flask, render_template
import requests
import random
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getFact')
def getFact():
    url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
    headers = {'Accept': 'application/json'}
    fact = requests.get(url, headers=headers).json()
    #fact_l = [{"id":"a8e7323f6a1c0d20c45194b2e0c2d9e3","text":"The Eiffel Tower in Paris was completed in 1889 and was designed by engineer Gustave Eiffel.","source":"history.com","source_url":"https://www.history.com/topics/landmarks/eiffel-tower","language":"en","permalink":"https://uselessfacts.jsph.pl/api/v2/facts/a8e7323f6a1c0d20c45194b2e0c2d9e3"},{"id":"b8f046c21469738f5693f57ab04d7d7c","text":"The honeybee is the only insect that produces food that we eat as humans - honey.","source":"sciencedaily.com","source_url":"https://www.sciencedaily.com/terms/honey.htm","language":"en","permalink":"https://uselessfacts.jsph.pl/api/v2/facts/b8f046c21469738f5693f57ab04d7d7c"},{"id":"d5be7eab15f9f92978e05986df4b413e","text":"The first recorded game of baseball was played in 1846 in Hoboken, New Jersey.","source":"mlb.com","source_url":"https://www.mlb.com/history/first-game","language":"en","permalink":"https://uselessfacts.jsph.pl/api/v2/facts/d5be7eab15f9f92978e05986df4b413e"},{"id":"e156a4b264913b6a5b0c20cc5ac6b8bb","text":"The average person spends about six months of their life waiting for red lights to turn green.","source":"nationalgeographic.com","source_url":"https://www.nationalgeographic.com/culture/article/traffic-stoplight-red-means-stop-but-why-is-there-red-and-green","language":"en","permalink":"https://uselessfacts.jsph.pl/api/v2/facts/e156a4b264913b6a5b0c20cc5ac6b8bb"},{"id":"f3082c28d39e0c1db2d4a82cb6e6d9d1","text":"Bananas are berries, but strawberries are not. In botanical terms, a berry is a fruit produced from the ovary of a single flower with seeds embedded in the flesh.","source":"smithsonianmag.com","source_url":"https://www.smithsonianmag.com/smart-news/strawberries-arent-berries-but-bananas-are-180952558/","language":"en","permalink":"https://uselessfacts.jsph.pl/api/v2/facts/f3082c28d39e0c1db2d4a82cb6e6d9d1"}]
    # fact = random.choice(fact_l)
    print(fact)
    return fact

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
