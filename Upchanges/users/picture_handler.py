import os
from PIL import Image
#The code above lets you import image
from flask import url_for, current_app


def add_profile_pic(pic_upload, username):
    filename = pic_upload.filename
    # "mypicture . jpg" this code below is use to check the file types
    ext_type = filename.split('.')[-1]
    # the code below saves the picture the user uploaded as username.jpg
    storage_filename = str(username)+'.'+ext_type

    filepath = os.path.join(current_app.root_path,'static/profile_pics',storage_filename)

    output_size = (400,400)


    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath) #save the pictures the users provided in a filepath in Upchanges application

    return storage_filename
    #returning a string like username.png

def add_blog_pic(pic_blog_upload, problem_name):
    filename = pic_blog_upload.filename
    # "mypicture . jpg" this code below is use to check the file types
    ext_type = filename.split('.')[-1]
    # the code below saves the picture the user uploaded as username.jpg
    storage_filename = str(problem_name)+'.'+ext_type

    filepath = os.path.join(current_app.root_path,'static/blog_pics',storage_filename)

    output_size = (550,250)


    pic_blog = Image.open(pic_blog_upload)
    pic_blog.thumbnail(output_size)
    pic_blog.save(filepath) #save the pictures the users provided in a filepath in Upchanges application

    return storage_filename
    #returning a string like username.png


def add_project_pic(pic_project_upload, project_name):
    filename = pic_project_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(project_name)+'.'+ext_type

    filepath  = os.path.join(current_app.root_path,'static/project_pics',storage_filename)

    output_size = (550,250)

    pic_project = Image.open(pic_project_upload)
    pic_project.thumbnail(output_size)
    pic_project.save(filepath)

    return storage_filename





