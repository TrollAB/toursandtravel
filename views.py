from flask import Blueprint
from flask.templating import render_template
views = Blueprint('views',__name__)
@views.route('/')
def Home():
    return render_template('home.html')
@views.route('/contact')
def contact():
    return "contact us"
@views.route('/about')
def about():
    return "about Us"
@views.route('/packages')
def packages():
    return "Our packages"