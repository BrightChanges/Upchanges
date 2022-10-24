from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import login_user, current_user, logout_user, login_required
from Upchanges import db, mail, app, s
from Upchanges.models import User, BlogPost, EmailConfirm
from Upchanges.users.forms import RegisterForm, LoginForm, UpdateUserForm, Resend_Email_Form
from Upchanges.users.picture_handler import add_profile_pic
from flask_mail import Mail,Message
from itsdangerous import URLSafeSerializer, SignatureExpired, TimedSerializer

users = Blueprint('users', __name__)


mail = mail
print(mail)

s=s

@users.route("/resend_confirmation_email", methods=['GET','POST'])
def resend_confirm():
    form = Resend_Email_Form()

    if form.validate_on_submit():
        email = form.email.data

        token = s.dumps(email, salt='email-confirm')

        msg = Message("Confirm your Upchanges account | Resend confirmation email", sender="letrungkien208@gmail.com",
                      recipients=[email])
        link = url_for("users.confirm_email", token=token, _external=True)
        msg.body = "Hi," \
 \
                   "Please click this link to confirm your Upchanges account: {}    The link will expired in 30 minutes and you may not be able to confirm your email permanently!" \
 \
                   "   Thank you.".format(link)
        mail.send(msg)
        return redirect(url_for('users.wait_for_confirm', email=email))

    return render_template('resend_confirm_email.html', form=form)



@users.route("/please_confirm_your_email/<email>")
def wait_for_confirm(email):
    return render_template("please_confirm_email.html", email=email)


@users.route("/confirm_link_expired/resend_confirmation_email")
def expired_resend_confirm():
  return render_template("confirm_time_out.html")


@users.route('/register', methods=['GET', 'POST'])
def register():
    form1 = RegisterForm()

    if form1.validate_on_submit():
        user = User(email=form1.email.data,
                    first_name=form1.first_name.data,
                    middle_name=form1.middle_name.data,
                    last_name=form1.last_name.data,
                    password=form1.password.data)
        check = User.query.filter_by(email=user.email).first()
        if check:
            abort(403)
        db.session.add(user)
        db.session.commit()

        account_verify = EmailConfirm(email_confirmed=False,
                                      user_email=form1.email.data)

        email = user.email
        print(email)

        token = s.dumps(email,salt="email-confirm")

        msg = Message("Confirm your Upchanges account", sender="letrungkien208@gmail.com", recipients=[email])
        link = url_for("users.confirm_email", token=token, _external=True)
        msg.body = "Hi," \
 \
                   "Please click this link to confirm your Upchanges account: {}    The link will expired in 30 minutes and you may not be able to confirm your email permanently!" \
 \
                   "   Thank you.".format(link)
        app.logger.info(msg.body)
        mail.send(msg)


        db.session.add(account_verify)
        db.session.commit()
        flash('Thanks for registration! Please confirm your email!')


        return redirect(url_for('users.wait_for_confirm', email=email))

    return render_template('register.html', form1=form1)


@users.route("/confirm_email/<token>")
def confirm_email(token):
    try:
        email = s.loads(token, salt="email-confirm", max_age=300)
        #the problem is about this expiration time above

    except SignatureExpired:
        return redirect(url_for("users.expired_resend_confirm"))


    account_verify = EmailConfirm.query.filter_by(user_email=email).first_or_404()

    # print(account_verify)
    account_verify.email_confirmed = True

    db.session.add(account_verify)
    db.session.commit()
    flash("You have confirmed your account. Thank you.")

    return render_template('confirmation_success.html')

# login
@users.route('/login', methods=['GET', 'POST'])
def login():
    form2 = LoginForm()
    if form2.validate_on_submit():
        user = User.query.filter_by(email=form2.email.data).first()  # putting first here helps get the right format
        account_verify = EmailConfirm.query.filter_by(user_email=form2.email.data).first_or_404()
        email_confirmed = account_verify.email_confirmed

        if user is not None and user.check_password(form2.password.data) and email_confirmed is not False:

            login_user(user)
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
        current_user.email = form3.email.data
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







######################Un-comment the codes below after testing/or when test didn't work out#################
#register
# @users.route('/register', methods=['GET', 'POST'])
# def register():
#     form1 = RegisterForm()
#
#     if form1.validate_on_submit():
#         user = User(email=form1.email.data,
#                     first_name=form1.first_name.data,
#                     middle_name=form1.middle_name.data,
#                     last_name=form1.last_name.data,
#                     password=form1.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Thanks for registration!')
#         return redirect(url_for('users.login'))
#     return render_template('register.html', form1=form1)
#
#
# # login
# @users.route('/login', methods=['GET', 'POST'])
# def login():
#     form2 = LoginForm()
#     if form2.validate_on_submit():
#         email1 = User.query.filter_by(email=form2.email.data).first()  # putting first here helps get the right format
#
#         if email1 is not None and email1.check_password(form2.password.data):
#
#             login_user(email1)
#             flash('Log in Success!')
#
#             next = request.args.get('next')  # grab the information of what the user tried to access
#             if next == None or not next[0] == '/':  # either go to the homepage or go the page they wanted to go
#                 next = url_for('core.index')
#             return redirect(next)
#     return render_template('login.html', form2=form2)


##############################################################################


