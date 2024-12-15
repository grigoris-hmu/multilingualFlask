from flask import Flask, request, g, redirect, url_for
from flask_babel import Babel
from config import Config


# set up application
app = Flask(__name__)
app.config.from_object(Config)

# import and register blueprints
from myApp.blueprints.multilingual import multilingual
app.register_blueprint(multilingual)

# set up babel
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(
            app.config['LANGUAGES']) or app.config['LANGUAGES'][0]
    return g.lang_code

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home():
    if not g.get('lang_code', None):
        get_locale()
    return redirect(url_for('multilingual.index'))
