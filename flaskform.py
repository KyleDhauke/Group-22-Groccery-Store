from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CheckoutForm(FlaskForm):
    FullName = StringField('FullName',
                validators=[DataRequired(message="Please enter your first name")])
    Address = StringField('LastName',
                validators=[DataRequired(message="Please enter your last name")])
    Address = StringField('Address',
                validators=[DataRequired("Please enter your home address")])
    CardNumber = IntegerField('CardNumber',
                validators=[DataRequired(), Length(min = 16, max = 16, message = "Enter the 16 digits without spaces")])
    CVV = IntegerField('CVV',
                validators=[DataRequired(), Length(min = 3, max =3, message = "This is the 3 digits on the back")])
    submit = SubmitField('Register')
