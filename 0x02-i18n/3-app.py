#!/usr/bin/env python3
"""Simple flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class of the app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

def get_locale():
    """Evaluate locale based on user requests"""
    request.accept_languages.best_match(app.config['LANGUAGES'])

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)
@app.route('/')

def index():
    """Index page route"""
    return render_template('3-index.html')

 
if __name__ == '__main__':
    app.run()
