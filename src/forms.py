from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DecimalField, FileField, DateTimeField, HiddenField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from src.models import User,List

class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired("User name cannot be empty!"),
            Length(min=3, max=20),
        ]
    )
    email = StringField(
        'Email Address',
        validators=[
            DataRequired("Mailboxes cannot be empty!"),
            Email("The mailbox format is incorrect!"),
            #validate_email
        ]
    )
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'There is already a user account registered with the email address "' + email.data + '".')

    password = PasswordField(
        'Password',
        validators=[
            DataRequired("Password cannot be empty!"),
            Length(min=6, max=60)
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired("Password cannot be empty!"),
            EqualTo('password',message="The two passwords don't match!")
        ]
    )
    submit = SubmitField('Register')



class LoginForm(FlaskForm):
    email = StringField(
        "Email Address",
        validators=[
            DataRequired(),
            Email("The mailbox format is incorrect!")
        ]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField("Login")

class CreatelistForm(FlaskForm):
    listname = StringField(
        "List Name",
        validators=[
            DataRequired(),
            #validate_listname
        ]
    )
    def validate_listname(self, listname):
        list = List.query.filter_by(name=listname.data).first()
        if list:
            raise ValidationError(
                'There is already a list named "' + listname.data + '".')

    submit = SubmitField("CreateList")

class MarkerInfo(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(),
            #validate_listname
        ]
    )
    description = StringField(
        "Description",
        validators=[
            DataRequired(),
            #validate_listname
        ]
    )
    tags = StringField(
        "Tags",
        validators=[
            DataRequired(),
            #validate_listname
        ]
    )
    lat = DecimalField(
        "Latitude",
        validators=[
            DataRequired(),
            #validate_listname
        ]
    )
    lng = DecimalField(
        "Longitude",
        validators=[
            DataRequired(),
            #validate_listname
        ]
    )
    userid = IntegerField(
        "userid",
        # validators=[
        #     DataRequired(),
        #     #validate_listname
        # ]
    )


    submit = SubmitField("complete")


class ChangeusernameForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired("User name cannot be empty!"),
            Length(min=3, max=20),
        ]
    )
    submit = SubmitField("Change")

class ChangeemailForm(FlaskForm):
    email = StringField(
        "Email Address",
        validators=[
            DataRequired(),
            Email("The mailbox format is incorrect!")
            #validate_email
        ]
    )
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'There is already a user account registered with the email address "' + email.data + '".')
    submit = SubmitField("Change")

class ChangepasswordForm(FlaskForm):
    password = PasswordField(
        "Password",
        validators=[
            # DataRequired()
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired("Password cannot be empty!"),
            EqualTo('password', message="The two passwords don't match!")
        ]
    )
    submit = SubmitField("Change")


class ReviewForm(FlaskForm):
    submit=SubmitField("Checkout")

