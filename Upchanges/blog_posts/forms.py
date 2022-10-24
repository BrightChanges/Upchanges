from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class BlogPostForm(FlaskForm):
    blog_image = FileField('Add picture of the problem+ / Update picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    #In the future, I may need to create a WebP image conversion, converting all image from the users to webp in the back end, reducing the size of all images'size: https://qiita.com/hengsokvisal/items/e4610ec5c39a2f0045cc
    problem_name = StringField('Problem Name', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    problem_type = SelectField('Type of Problem', choices=[('education','Education'),('health','Health'),('environment','Environment'),('economics','Economics'),('society','Society')],validators=[DataRequired()])
    country = SelectField('Country location', choices=[('Vietnam', 'Vietnam'), ('Japan', 'Japan'),('United States of America', 'United States of America'),('Estonia','Estonia'),('Ghana','Ghana'),('Mongolia','Mongolia'),('Others','Others')], validators=[DataRequired()])
    problem_submit = SubmitField("Post")


class BlogIdeaForm(FlaskForm):
    text2 = TextAreaField('Add your idea', validators=[DataRequired()])
    idea_submit = SubmitField("Post")

class BlogProjectForm(FlaskForm):
    project_image = FileField('Add picture of your project+ / Update picture:', validators=[FileAllowed(['jpg', 'png', 'jpeg']), DataRequired()])
    project_name = StringField('Your project name:', validators=[DataRequired()])
    project_short_info = TextAreaField('Short description of your project:', validators=[DataRequired()])
    project_link = StringField('Google Docs link to your project:', validators=[DataRequired()])
    project_submit = SubmitField("Post")

