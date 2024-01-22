from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_term = request.form['search_term']
        result = get_result(search_term)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)


def get_result(search_term):
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{search_term}')
    result = response.json()
    if result[0]['phonetics'][0]['audio']:
        audioResult = result[0]['phonetics'][0]['audio']
    else:
        audioResult = result[0]['phonetics'][1]['audio']

    return {
        'word': result[0]['word'],
        'phonetic': result[0]['phonetic'],
        'phonetic_audio': audioResult,
        'meanings': result[0]['meanings']
    }

if __name__ == "__main__":
    app.run(debug=True)

