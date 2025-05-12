from flask import Flask, render_template, request
from summarizer.extractive import extractive_summary
from summarizer.abstractive import abstractive_summary

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    input_text = ""
    if request.method == 'POST':
        input_text = request.form['input_text']
        method = request.form['method']

        if method == 'extractive':
            summary = extractive_summary(input_text)
        elif method == 'abstractive':
            summary = abstractive_summary(input_text)

    return render_template('index.html', summary=summary, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
