from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, SubmitField
from flask import render_template
from wtforms.validators import DataRequired, Email, ValidationError

from Upchanges.models import BlogPost, User, UpchangesX_email


class Blogsearch_form(Form):
    search = StringField('')      #THIS MODEL BLOG SEARCH IS NOT STORING ANY DATA.

#This Blogsearch_form should be the other model Blog_Post


class UpchangesX_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    email_submit = SubmitField('Subscribe')

    def check_email(self, field):
        if UpchangesX_email.query.filter_by(email=field.data).first(): #This code is to make sure that an email can only be registered for 1 time.
            raise ValidationError('Your email had been registered already.')