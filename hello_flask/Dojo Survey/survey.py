from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def survery():
    return render_template('survey.html')

@app.route('/results', methods= ['POST'])
def result():
    return render_template('result.html')

app.run(debug=True)