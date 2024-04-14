from flask import render_template

from IRA import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query')
def query():
    return render_template('query.html')

@app.route('/result')
def result():
    return render_template('result.html')