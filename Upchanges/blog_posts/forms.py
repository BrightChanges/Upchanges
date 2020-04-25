from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class BlogPostForm(FlaskForm):
    # blog_image = FileField('Picture of the problem(jpg,jpeg,png)', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    problem_name = StringField('Problem Name', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    problem_submit = SubmitField("Post")