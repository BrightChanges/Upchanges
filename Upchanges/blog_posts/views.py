from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from Upchanges import db
from Upchanges.models import BlogPost
from Upchanges.blog_posts.forms import BlogPostForm
from Upchanges.users.picture_handler import add_blog_pic

blog_posts = Blueprint('blog_posts',__name__)

#Create
@blog_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():

        blog_validated = BlogPost(problem_name=form.problem_name.data,
                                  text=form.text.data,
                                  user_id=current_user.id,
                                  blog_image=add_blog_pic(form.blog_image.data, form.problem_name.data+str(current_user.id))) #####


        blog_image = url_for('static', filename='profile_pics/' + blog_validated.blog_image)
        db.session.add(blog_validated)
        db.session.commit()
        flash('Blog Post Created')
        return redirect(url_for('core.index', blog_image=url_for('static', filename='profile_pics/' + blog_validated.blog_image)))

    return render_template('create_post.html', form=form)




#View blog post
@blog_posts.route('/<int:blog_validated_id>') #int makes a string a number so that BlogPost.query doesn't show error(because data can only stored as number)
def blog_view(blog_validated_id):
    blog_view = BlogPost.query.get_or_404(blog_validated_id) #check to see if a blog with an id exist, if not, return 404
    # blog_next = blog_validated_id+1
    return render_template('blog_view.html', problem_name=blog_view.problem_name,
                           date=blog_view.date,
                           blog_image=blog_view.blog_image,
                           post=blog_view)
# put post_next=blog_next after post=blog_view, later(trying to create a blog_id+1's id for the alignment of blogs)


#Update
@blog_posts.route('/<int:blog_validated_id>/update', methods=['GET', 'POST'])
@login_required
def update(blog_validated_id):
    blog_update = BlogPost.query.get_or_404(blog_validated_id)

    if blog_update.creator != current_user: #if creator of the blog is not the current user
        abort(403)  #show 403 no permission page

    form = BlogPostForm()  #Creating an instance by writing A= B() ;creating an instance of B using A

    if form.validate_on_submit():

        if form.blog_image.data:
            blog_update.blog_image = add_blog_pic(form.blog_image.data, form.problem_name.data + str(current_user.id))
            # blog_update.blog_image=blog_image

        blog_update.problem_name = form.problem_name.data
        blog_update.text = form.text.data
        db.session.commit()
        flash('Blog Post Updated')
        return redirect(url_for('blog_posts.blog_view',blog_validated_id=blog_update.blog_id, blog_image=url_for('static', filename='blog_pics/' + blog_update.blog_image)))

    elif request.method =='GET':
        form.problem_name.data = blog_update.problem_name
        form.text.data = blog_update.text
        form.blog_image.data=blog_update.blog_image

    return render_template('create_post.html', form=form)




#Delete
@blog_posts.route('/<int:blog_validated_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(blog_validated_id):

    blog_delete = BlogPost.query.get_or_404(blog_validated_id)

    if blog_delete.creator != current_user: #if creator of the blog is not the current user
        abort(403)  #show 403 no permission page

    db.session.delete(blog_delete)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('core.index'))


