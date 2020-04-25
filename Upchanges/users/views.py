from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from Upchanges import db
from Upchanges.models import User, BlogPost
from Upchanges.users.forms import RegisterForm, LoginForm, UpdateUserForm
from Upchanges.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)


# register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form1 = RegisterForm()

    if form1.validate_on_submit():
        user = User(email=form1.email.data,
                    first_name=form1.first_name.data,
                    middle_name=form1.middle_name.data,
                    last_name=form1.last_name.data,
                    password=form1.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form1=form1)


# login
@users.route('/login', methods=['GET', 'POST'])
def login():
    form2 = LoginForm()
    if form2.validate_on_submit():
        email1 = User.query.filter_by(email=form2.email.data).first()  # putting first here helps get the right format

        if email1 is not None and email1.check_password(form2.password.data):

            login_user(email1)
            flash('Log in Success!')

            next = request.args.get('next')  # grab the information of what the user tried to access
            if next == None or not next[0] == '/':  # either go to the homepage or go the page they wanted to go
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html', form2=form2)


# logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.index"))


# account (update UserForm)
@users.route('/account', methods=['GET',
                                  'POST'])  # put in get, post methods when the page your direct to let the users interact through a form or data
@login_required
def account():
    form3 = UpdateUserForm()
    if form3.validate_on_submit():

        if form3.picture.data:  # if a user upload a picture through the UpdateUserForm
            first_name = current_user.first_name
            middle_name = current_user.middle_name
            last_name = current_user.last_name
            pic = add_profile_pic(form3.picture.data, first_name + middle_name + last_name)
            current_user.profile_image = pic

        current_user.first_name = form3.first_name.data
        current_user.middle_name = form3.middle_name.data
        current_user.last_name = form3.last_name.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form3.first_name.data = current_user.first_name
        form3.middle_name.data = current_user.middle_name
        form3.last_name.data = current_user.last_name
        form3.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form3=form3)


# user's list of Blog Posts
@users.route('/<username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)  # request 1 page to scroll
    home_user = User.query.filter_by(username=username).first_or_404()  # check if the user is created  #THIS IS WORKIING SO IT MEANS SOMETHING IS WRONG ABOUT THE username=username

    blog_posts = BlogPost.query.filter_by(creator=home_user).order_by(BlogPost.date.desc()).paginate(page=page,
                                                                                                     per_page=5)  # make sure you can scroll and see 5 pages using paginate
    return render_template('user_blog_posts.html', blog_posts=blog_posts, home_user=home_user)


# @login_required
# @users.route('/<username>')
# def user_mypage(username):
#     page = request.args.get('page', 1, type=int)
#     user_me = User.query.filter_by(username=username).first_or_404()
#
#     blog_posts = BlogPost.query.filter_by(creator=user_me).order_by(BlogPost.date.desc()).paginate(page=page,
#                                                                                                      per_page=5)
#     return render_template('mypage.html', blog_posts=blog_posts, user_me=user_me)


