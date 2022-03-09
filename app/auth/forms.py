from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import Required, Email, EqualTo, ValidationError
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    username = StringField('Enter your Username', validators = [Required()])
    password = PasswordField('Password', validators = [Required(), EqualTo('password_confirm', message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password', validators = [Required()])
    submit = SubmitField('Sign Up')

    #Adding custom validators for username and email to prevent duplication

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("There is an account using that email !")

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("That username is already taken")


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators = [Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField("Sign in")