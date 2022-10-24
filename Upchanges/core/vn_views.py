from flask import render_template, request, Blueprint, url_for, flash, redirect
from sqlalchemy import or_, null, and_

from Upchanges.core.forms import Blogsearch_form
from Upchanges.models import BlogPost
import _sqlite3

vn_core = Blueprint('vn_core',__name__)

@vn_core.route('/vietnam', methods=['GET', 'POST'])
def index():
    # Call a function to later use in creating the template

    form = Blogsearch_form(request.form)



    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id).filter(and_(BlogPost.country.ilike('Vietnam')),(BlogPost.problem_name.ilike("%" + form.search.data  + "%"))).all()] #Still need to change this for country(and all codes below)

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(and_(BlogPost.country.ilike('Vietnam')),(or_((BlogPost.problem_name.ilike(search_string)),(BlogPost.text.ilike(search_string))))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts="Couldn't find relating problems"
        else:
            no_posts=''
        country = 'Vietnam'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts, no_posts=no_posts, form=form, country=country)

    country = 'Vietnam'
    page = request.args.get('page',1,type=int)
    many_posts = BlogPost.query.filter(BlogPost.country.ilike('Vietnam')).order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', many_posts=many_posts, form=form, country=country)


@vn_core.route('/vietnam/education', methods=['GET', 'POST'])
def education():

    form = Blogsearch_form(request.form)
    page = request.args.get('page', 1, type=int)
    many_posts = BlogPost.query.filter(and_(BlogPost.country.ilike('Vietnam')),(BlogPost.problem_type.ilike('education'))).order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)

    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id).filter(and_(BlogPost.country.ilike('Vietnam')),(BlogPost.problem_name.ilike("%" + form.search.data  + "%"))).all()] #This code on the left side doesn't do anything, it's just there to help me to learn to code

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(and_(BlogPost.country.ilike('Vietnam')),(or_((BlogPost.problem_name.ilike(search_string)),(BlogPost.text.ilike(search_string))))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts="Couldn't find relating problems"
        else:
            no_posts=''
        country = 'Vietnam'
        problem_type = 'education'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts,
                           no_posts=no_posts, form=form, country=country, problem_type=problem_type)

    country = 'Vietnam'
    problem_type = 'education'
    return render_template('index1.html', many_posts=many_posts, form=form, country=country, problem_type=problem_type)

@vn_core.route('/vietnam/health', methods=['GET', 'POST'])
def health():
    form = Blogsearch_form(request.form)
    page = request.args.get('page', 1, type=int)
    many_posts = BlogPost.query.filter(and_(BlogPost.country.ilike('Vietnam')),(BlogPost.problem_type.ilike('health'))).order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)

    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id).filter(and_(BlogPost.country.ilike('Vietnam')),(BlogPost.problem_name.ilike("%" + form.search.data  + "%"))).all()] #This code on the left side doesn't do anything, it's just there to help me to learn to code

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(and_(BlogPost.country.ilike('Vietnam')),(or_((BlogPost.problem_name.ilike(search_string)),(BlogPost.text.ilike(search_string))))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts="Couldn't find relating problems"
        else:
            no_posts=''
        country = 'Vietnam'
        problem_type = 'health'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts,
                           no_posts=no_posts, form=form, country=country, problem_type=problem_type)

    country = 'Vietnam'
    problem_type = 'health'
    return render_template('index1.html', many_posts=many_posts, form=form, country=country, problem_type=problem_type)


@vn_core.route('/vietnam/environment', methods=['GET', 'POST'])
def environment():
    form = Blogsearch_form(request.form)
    page = request.args.get('page', 1, type=int)
    many_posts = BlogPost.query.filter(and_(BlogPost.country.ilike('Vietnam')),(BlogPost.problem_type.ilike('environment'))).order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)

    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id).filter(and_(BlogPost.country.ilike('Vietnam')),(BlogPost.problem_name.ilike("%" + form.search.data  + "%"))).all()] #This code on the left side doesn't do anything, it's just there to help me to learn to code

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(and_(BlogPost.country.ilike('Vietnam')),(or_((BlogPost.problem_name.ilike(search_string)),(BlogPost.text.ilike(search_string))))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts="Couldn't find relating problems"
        else:
            no_posts=''
        country = 'Vietnam'
        problem_type = 'environment'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts,
                           no_posts=no_posts, form=form, country=country, problem_type=problem_type)

    country = 'Vietnam'
    problem_type = 'environment'
    return render_template('index1.html', many_posts=many_posts, form=form, country=country, problem_type=problem_type)

@vn_core.route('/vietnam/economics', methods=['GET', 'POST'])
def economics():
    form = Blogsearch_form(request.form)
    page = request.args.get('page', 1, type=int)
    many_posts = BlogPost.query.filter(and_(BlogPost.country.ilike('Vietnam')),(BlogPost.problem_type.ilike('economics'))).order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)

    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id).filter(and_(BlogPost.country.ilike('Vietnam')),(BlogPost.problem_name.ilike("%" + form.search.data  + "%"))).all()]  # This code on the left side doesn't do anything, it's just there to help me to learn to code

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(and_(BlogPost.country.ilike('Vietnam')),(or_((BlogPost.problem_name.ilike(search_string)),(BlogPost.text.ilike(search_string))))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts = "Couldn't find relating problems"
        else:
            no_posts = ''
        country = 'Vietnam'
        problem_type = 'economics'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts,
                               no_posts=no_posts, form=form, country=country, problem_type=problem_type)
    country = 'Vietnam'
    problem_type = 'economics'
    return render_template('index1.html', many_posts=many_posts, form=form, country=country, problem_type=problem_type)

@vn_core.route('/vietnam/society', methods=['GET', 'POST'])
def society():
    form = Blogsearch_form(request.form)
    page = request.args.get('page', 1, type=int)
    many_posts = BlogPost.query.filter(and_(BlogPost.country.ilike('Vietnam')),
                                       (BlogPost.problem_type.ilike('society'))).order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)

    if request.method == 'POST':
        id_list = [i[0] for i in BlogPost.query.with_entities(BlogPost.blog_id).filter(and_(BlogPost.country.ilike('Vietnam')),(BlogPost.problem_name.ilike("%" + form.search.data  + "%"))).all()] # This code on the left side doesn't do anything, it's just there to help me to learn to code

        page = request.args.get('page', 1, type=int)
        search_string = "%" + "%".join(form.search.data.split()) + "%"
        many_posts0 = BlogPost.query.filter(and_(BlogPost.country.ilike('Vietnam')),(or_((BlogPost.problem_name.ilike(search_string)),(BlogPost.text.ilike(search_string))))).order_by(BlogPost.date.desc())
        many_posts = many_posts0.paginate(page=page, per_page=10)
        num_posts = many_posts0.count()
        if num_posts == 0:
            no_posts = "Couldn't find relating problems"
        else:
            no_posts = ''
        country = 'Vietnam'
        problem_type = 'society'
        return render_template('blog_search_result.html', id_list=id_list, many_posts=many_posts, num_posts=num_posts,
                               no_posts=no_posts, form=form, country=country, problem_type=problem_type)
    country = 'Vietnam'
    problem_type = 'society'
    return render_template('index1.html', many_posts=many_posts, form=form, country=country, problem_type=problem_type)






@vn_core.route('/vietnam/info')
def info():
    country = 'Vietnam'
    return render_template('info.html', country=country)