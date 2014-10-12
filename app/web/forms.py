from flask.ext.wtf import Form, html5
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class FlightsForm(Form):
    name = StringField('Name?', validators=[DataRequired()])
    tel = html5.TelField('Mobile')
    submit = SubmitField('Submit')


class CarForm(Form):
    name = StringField('Name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class HotelForm(Form):
    name = StringField('Name?', validators=[DataRequired()])
    submit = SubmitField('Submit')