from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed  #This line allows user to choose and select file from their computer
from flask_login import current_user
from Upchanges.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In ->')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First name', validators=[DataRequired()])
    middle_name = StringField('Middle name')
    last_name = StringField('Last name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Password must match!')])
    blog_submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first(): #This code is to make sure that an email can only be registered for 1 time.
            raise ValidationError('Your email had been registered already.')


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First name', validators=[DataRequired()])
    middle_name = StringField('Middle name')
    last_name = StringField('Last name', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    # Specify the type of file of the image the user can upload
    update_submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first(): #This code is to make sure that an email can only be registered for 1 time.
            raise ValidationError('Your email had been registered already.')


class Resend_Email_Form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    resend_post = SubmitField('Send Account Confirmation Email')

    def check_email(self, field):
        if not User.query.filter_by(email=field.data).first(): #This code is to make sure that an email can only be registered for 1 time.
            raise ValidationError("Your email hadn't been registered.")


