from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from Upchanges import db
from Upchanges.models import BlogInfo, BlogPost
from Upchanges.blog_info.forms import BlogInfoForm



blog_info = Blueprint('blog_info',__name__)
#
# @blog_info.route('/add_comment', methods=['GET','POST'])
# @login_required
# def add_comment():
#
#     form2 = BlogInfo()
#     BlogInfo.blog_post_id=BlogPost.blog_id
#
#     if form2.validate_on_submit():
