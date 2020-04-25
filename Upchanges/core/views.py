#create the view function for some main pages
from flask import render_template, request, Blueprint
from Upchanges.models import BlogPost

core = Blueprint('core', __name__)

#MAIN PAGE
@core.route('/')
def index():
    #Call a function to later use in creating the template
    page = request.args.get('page',1,type=int)
    many_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', many_posts=many_posts)

@core.route('/info')
def info():
    return render_template('info.html')