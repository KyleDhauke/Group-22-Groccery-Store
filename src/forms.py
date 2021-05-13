from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DecimalField, FileField, DateTimeField, HiddenField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from src.models import User,List

# def validate_email(self, email):
#     user = User.query.filter_by(email=email.data).first()
#     if user:
#         raise ValidationError('There is already a user account registered with the email address "' + email.data + '".')

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
        "Title",
        validators=[
            DataRequired(),
            #validate_listname
        ]
    )
    lat = IntegerField(
        "Latitude",
        validators=[
            DataRequired(),
            #validate_listname
        ]
    )
    lng = IntegerField(
        "Longitude",
        validators=[
            DataRequired(),
            #validate_listname
        ]
    )
    userid = IntegerField(
        "userid",
        validators=[
            DataRequired(),
            #validate_listname
        ]
    )


    submit = SubmitField("complete")


#class CheckoutForm(FlaskForm):
#
#    name = StringField("Full Name", validators=[DataRequired(), Regexp(r'^[A-Za-z]', message=("Error Name: Please enter alphabetical characters")), Length(min=1, max=50, message=("Name: Please enter 1 to 50 characters"))])
#    email = StringField("Email Address", validators=[DataRequired()])
#    address = StringField("Address", validators=[DataRequired()])
#    city = StringField("City", validators=[DataRequired(), Regexp(r'^[A-Za-z]', message=("Error City: Please enter alphabetical characters"))])
#    postcode = StringField("Postcode", validators=[DataRequired(), Length(min=6, max=8, message=("Error Postcode: Please enter 6 to 8 characters"))])
#    cname = StringField("Name on Card", validators=[DataRequired(), Regexp(r'^[A-Za-z]', message=("Error Name: Please enter alphabetical characters")), Length(min=1, max=50)])
#    ccnum = StringField("Credit card number", validators=[DataRequired(), Length(min=16, max=16, message=("Error Card number: Please enter 16 characters"))])
#    expmonth = DateTimeField ("Expiry Date", format="%m/%y", validators=[DataRequired()])
#    cvv = StringField("CVV", validators=[DataRequired(), Length(min=3, max=3, message=("Error CVV: Please enter 3 characters"))])
#
#    submit = SubmitField("Continue to checkout")
#
#
#class SearchForm(FlaskForm):
#    search = StringField("")
#    submit = SubmitField("")
#
#    price = DecimalField(0.0, validators=[DataRequired()])
#    image = FileField("Cover Image")
#    name = StringField("", validators=[DataRequired()])
#    description = TextAreaField("", validators=[DataRequired()])
#    submit = SubmitField("Save")
#
#class PublishProductForm(FlaskForm):
#    publishbutton = SubmitField("Publish")
#
#class UnpublishProductForm(FlaskForm):
#    publishbutton = SubmitField("Unpublish")
#
#class DeleteProductForm(FlaskForm):
#    cancel = SubmitField("Cancel")
#    submit = SubmitField("Delete Forever")
#
#class AllProductsForm(FlaskForm):
#    submit=SubmitField("Sort")
#
class ReviewForm(FlaskForm):
    submit=SubmitField("Checkout")
#
#class AddCartForm(FlaskForm):
#    product_id = HiddenField()
#    quantity = IntegerField()
#    submit=SubmitField("AddtoBasket")
