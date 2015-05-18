import os
from flask import (
    Flask,
    url_for,
    render_template,
    redirect,
    request,
    flash
    )

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('application.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/start')
def start():
    return render_template('faq.html')

@app.route('/new-year')
def christmas():
    return render_template('new-year.html')

@app.route('/holidays')
def holidays():
    return render_template('holidays.html')

@app.route('/offers')
def offers():
    return render_template('offers.html')



if __name__ == '__main__':
    app.run(debug=True)