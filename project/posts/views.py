# posts views

from project import db,mail,app
from flask import Blueprint,render_template,request
from project.posts.models import Posts
from datetime import datetime
import os

posts_blueprint=Blueprint('posts',__name__,template_folder='tamplates/posts')

@posts_blueprint.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html", params=params, post=post)

@posts_blueprint.route('/add_post',methods=['GET','POST'])
def add():
    if request.method == 'POST':
            box_title = request.form.get('title')
            tline = request.form.get('tagline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            post = Posts(title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file,date=datetime.now())
            db.session.add(post)
            try:
                db.session.commit()
            except:
                flash('title should be unique')

    return render_template('add.html',params=params)



@posts_blueprint.route("/edit/<string:sno>", methods=["GET", "POST"])
def edit(sno):
    # ############################# Checking the session as user is valid or not ##############################
    if ('user' in session and session['user'] == params['admin-user']):
        ''' Checking for the post request from the web page and taking the details from user and storing in db '''
        if request.method == 'POST':
            ''' Fetch entry from the post page '''
            box_title = request.form.get('title')
            tline = request.form.get('tagline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')

            if sno == '0':
                post = Posts(title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file,date=datetime.now())
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.tagline = tline
                post.slug = slug
                post.content = content
                post.img_file = img_file
                db.session.commit()
                return redirect('posts/edit/' + sno)
        post = Posts.query.filter_by(sno=sno).first()
    return render_template('edit.html', params=params, post=post, sno=sno)

@posts_blueprint.route("/uploader", methods=["GET", "POST"])
def uploader():
    if ('user' in session and session['user'] == params['admin-user']):
        if (request.method == 'POST'):
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER']))#, secure_filename(f.filename)))
            return "Uploaded successfully"

@posts_blueprint.route("/delete/<string:sno>", methods=["GET", "POST"])
def delete(sno):
    if ('user' in session and session['user'] == params['admin-user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')
