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

# @app.route('/static/work/kleenteem')
# def kleenteem():
#     return render_template('static/kleenteem/index.html')

if __name__ == '__main__':
    app.run(debug=True)