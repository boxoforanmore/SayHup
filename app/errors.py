from flask import render_template
from app import app


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(401)
def login_error(error):
    return render_template('errors/401.html'), 401