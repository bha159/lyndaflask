from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First Name', validators=[DataRequired("Give ur fucking first name")])
    last_name = StringField('Last Name', validators=[DataRequired("Give ur fucking last name")])
    email = StringField('Email', validators=[DataRequired("Moron! Email is needed"), Email("U don't know how a email look?")])
    password = PasswordField('Password', validators=[DataRequired("U dumb bitch, type a password"), Length(min=6, message="Make a 6 character or long fucking strong password")])
    submit = SubmitField('Sign Up')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Moron! Email is needed"), Email("U don't know how a email look?")])
    password = PasswordField('Password', validators=[DataRequired("U dumb bitch, type a password")])
    submit = SubmitField('Sign In')
