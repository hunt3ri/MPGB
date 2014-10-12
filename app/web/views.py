from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/book/with/<partner>')
def booking(partner):
    return render_template('booking.html', partner=partner)

@main.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


