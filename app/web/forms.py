from flask.ext.wtf import Form, html5
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class FlightsForm(Form):
    name = StringField('Name?', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    tel = html5.TelField('Mobile')
    payment_type = SelectField(u'Payment Type', choices=[('amex', 'American Express'), ('mastercard', 'Master Card'), ('visa', 'Visa')])
    additional_baggage = SelectField('Additional Bags', choices=[('0', '0'), ('1', '1'), ('2', '2')])
    submit = SubmitField('Submit')


class CarForm(Form):
    name = StringField('Name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class HotelForm(Form):
    name = StringField('Name?', validators=[DataRequired()])
    submit = SubmitField('Submit')