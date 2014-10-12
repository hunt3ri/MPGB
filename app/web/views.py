from flask import render_template, session, redirect, url_for
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from . import main


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/book/with/<partner>', methods=['GET', 'POST'])
def booking(partner):
    name = None
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.confirmation'))
    return render_template('booking.html', partner=partner, form=form)

@main.route('/success')
def confirmation():
    return render_template('handover.html', name=session.get('name'))

