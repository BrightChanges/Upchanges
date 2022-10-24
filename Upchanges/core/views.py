#create the view function for some main pages
import os

from flask import render_template, request, Blueprint, url_for, flash, redirect, abort
from sqlalchemy import or_, null

from Upchanges import db, mail, app, s
from Upchanges.core.forms import Blogsearch_form, UpchangesX_form
from Upchanges.models import BlogPost, UpchangesX_email
import _sqlite3



import os
print("MY FILE = ", os.path.realpath(__file__))
MYDIR = os.path.dirname(__file__)
print("MYDIR = ", os.path.realpath(MYDIR))
SQLPATH = os.path.join(MYDIR, "..", "data.sqlite")
print("This gives me SQLPATH = ", os.path.realpath(SQLPATH))
conn = _sqlite3.connect(SQLPATH, check_same_thread=False)  #This path is righ! How can still it is not working>
c = conn.cursor()




core = Blueprint('core', __name__)

#MAIN PAGE
@core.route('/', methods=['GET', 'POST'])
def index():
    # Call a function to later use in creating the template
    form = Blogsearch_form(request.form)



    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id).filter(BlogPost.problem_name.ilike("%" + form.search.data  + "%")).all()] #This code on the left side doesn't do anything, it's just there to help me to learn to code

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(or_((BlogPost.problem_name.ilike(search_string)),(BlogPost.text.ilike(search_string)))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts="Couldn't find relating problems"
        else:
            no_posts=''
        country='Earth'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts, no_posts=no_posts, form=form, country=country)


    country='Earth'
    page = request.args.get('page',1,type=int)
    many_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', many_posts=many_posts, form=form, country=country)


@core.route('/education', methods=['GET', 'POST'])
def education():

    form = Blogsearch_form(request.form)
    page = request.args.get('page', 1, type=int)
    many_posts = BlogPost.query.filter(BlogPost.problem_type.ilike('education')).order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)

    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id ).filter(BlogPost.problem_name.ilike("%" + form.search.data  + "%")).all()] #This code on the left side doesn't do anything, it's just there to help me to learn to code

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(or_((BlogPost.problem_name.ilike(search_string)), (BlogPost.text.ilike(search_string)))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts="Couldn't find relating problems"
        else:
            no_posts=''
        country = 'Earth'
        problem_type = 'education'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts,
                           no_posts=no_posts, form=form, country=country, problem_type=problem_type)

    country = 'Earth'
    problem_type = 'education'
    return render_template('index1.html', many_posts=many_posts, form=form, country=country, problem_type=problem_type)

@core.route('/health', methods=['GET', 'POST'])
def health():
    form = Blogsearch_form(request.form)
    page = request.args.get('page', 1, type=int)
    many_posts = BlogPost.query.filter(BlogPost.problem_type.ilike('health')).order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)

    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id ).filter(BlogPost.problem_name.ilike("%" + form.search.data  + "%")).all()] #This code on the left side doesn't do anything, it's just there to help me to learn to code

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(or_((BlogPost.problem_name.ilike(search_string)), (BlogPost.text.ilike(search_string)))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts="Couldn't find relating problems"
        else:
            no_posts=''
        country = 'Earth'
        problem_type = 'health'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts,
                           no_posts=no_posts, form=form, country=country, problem_type=problem_type)

    country = 'Earth'
    problem_type = 'health'
    return render_template('index1.html', many_posts=many_posts, form=form, country=country, problem_type=problem_type)

@core.route('/environment', methods=['GET', 'POST'])
def environment():
    form = Blogsearch_form(request.form)
    page = request.args.get('page', 1, type=int)
    many_posts = BlogPost.query.filter(BlogPost.problem_type.ilike('environment')).order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)

    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id ).filter(BlogPost.problem_name.ilike("%" + form.search.data  + "%")).all()] #This code on the left side doesn't do anything, it's just there to help me to learn to code

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(or_((BlogPost.problem_name.ilike(search_string)), (BlogPost.text.ilike(search_string)))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts="Couldn't find relating problems"
        else:
            no_posts=''
        country = 'Earth'
        problem_type = 'environment'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts,
                           no_posts=no_posts, form=form, country=country, problem_type=problem_type)
    country = 'Earth'
    problem_type = 'environment'
    return render_template('index1.html', many_posts=many_posts, form=form, country=country, problem_type=problem_type)

@core.route('/economics', methods=['GET', 'POST'])
def economics():
    form = Blogsearch_form(request.form)
    page = request.args.get('page', 1, type=int)
    many_posts = BlogPost.query.filter(BlogPost.problem_type.ilike('economics')).order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)

    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id ).filter(BlogPost.problem_name.ilike("%" + form.search.data  + "%")).all()] #This code on the left side doesn't do anything, it's just there to help me to learn to code

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(or_((BlogPost.problem_name.ilike(search_string)), (BlogPost.text.ilike(search_string)))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts="Couldn't find relating problems"
        else:
            no_posts=''
        country = 'Earth'
        problem_type = 'economics'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts,
                           no_posts=no_posts, form=form, country=country, problem_type=problem_type)
    country = 'Earth'
    problem_type = 'economics'
    return render_template('index1.html', many_posts=many_posts, form=form, country=country, problem_type=problem_type)

@core.route('/society', methods=['GET', 'POST'])
def society():
    form = Blogsearch_form(request.form)
    page = request.args.get('page', 1, type=int)
    many_posts = BlogPost.query.filter(BlogPost.problem_type.ilike('society')).order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)

    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id).filter(BlogPost.problem_name.ilike("%" + form.search.data  + "%")).all()] #This code on the left side doesn't do anything, it's just there to help me to learn to code

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(or_((BlogPost.problem_name.ilike(search_string)), (BlogPost.text.ilike(search_string)))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts="Couldn't find relating problems"
        else:
            no_posts=''
        country = 'Earth'
        problem_type = 'society'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts,
                           no_posts=no_posts, form=form, country=country, problem_type=problem_type)
    country = 'Earth'
    problem_type = 'society'
    return render_template('index1.html', many_posts=many_posts, form=form, country=country, problem_type=problem_type)



@core.route('/upchangesx', methods=['GET', 'POST'])
def upchangesx():
    country = 'Earth'

    form = UpchangesX_form()

    # submission_successful = False

    if form.validate_on_submit():
        user = UpchangesX_email(email=form.email.data)

        check = UpchangesX_email.query.filter_by(email=user.email).first()
        if check:
            abort(403)
        elif "@" not in form.email.data:
            print("Invalid email")
            abort(403)

        db.session.add(user)
        db.session.commit()
        print("Email registered for {}".format(user.email))
        # submission_successful = True

        return redirect(url_for('core.upchangesx_thankyou'))


    return render_template('upchangesx.html', country=country, form=form)


@core.route('/upchangesx/subscribed')
def upchangesx_thankyou():
    country = 'Earth'
    return render_template('upchangesx_thankyou.html', country=country)

@core.route('/info')
def info():
    country = 'Earth'
    return render_template('info.html', country=country)

@core.route('/contact')
def contact():
    country = 'Earth'
    return render_template('contact.html', country=country)

@core.route('/terms')
def terms():
    country = 'Earth'
    return render_template('terms.html', country=country)


@core.route('/privacy')
def privacy():
    country = 'Earth'
    return render_template('privacy_policy.html', country=country)

@core.route('/faq')
def faq():
    country = 'Earth'
    return render_template('faq.html', country=country)