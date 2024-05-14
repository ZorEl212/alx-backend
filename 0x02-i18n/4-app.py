#!/usr/bin/env python3
"""Simple flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for the app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

def get_locale():
    """Evaluate locale based on user requests"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(app, locale_selector=get_locale)
@app.route('/')

def index():
    """Index route of the app"""
    return render_template('3-index.html')

 
if __name__ == '__main__':
    app.run()
