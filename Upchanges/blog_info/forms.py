from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired

class BlogInfoForm(FlaskForm):
    text = TextAreaField('Comment| Add info', validators=[DataRequired()])
    comment_submit = SubmitField("Post")