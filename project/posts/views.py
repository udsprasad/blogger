# posts views

from project import db,mail,app,params
from flask import Blueprint,render_template,request,flash,session,redirect,url_for
from project.posts.models import Posts
from project.users.models import User
from datetime import datetime
import os
from flask_login import login_required

posts_blueprint=Blueprint('posts',__name__,template_folder='templates/posts')

@posts_blueprint.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    users=User.query.all()
    return render_template("post.html", params=params, post=post,users=users)

@posts_blueprint.route('/add_post/<user_id>',methods=['GET','POST'])
@login_required
def add(user_id):
    if request.method == 'POST':
            box_title = request.form.get('title')
            tline = request.form.get('tagline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            owner_id=user_id
            post = Posts(title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file,date=datetime.now(),owner_id=owner_id)
            db.session.add(post)
            try:
                db.session.commit()
            except:
                flash('title should be unique')

    return render_template('add.html',params=params,user_id=user_id)



@posts_blueprint.route("/edit/<string:sno>", methods=["GET", "POST"])
def edit(sno):

  if request.method == 'POST':
      ''' Fetch entry from the post page '''
      box_title = request.form.get('title')
      tline = request.form.get('tagline')
      slug = request.form.get('slug')
      content = request.form.get('content')
      img_file = request.form.get('img_file')

      if sno == '0':
          post = Posts(title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file,date=datetime.now(),owner_id=current_user.get_id())
          db.session.add(post)
          db.session.commit()
      else:
          post = Posts.query.filter_by(sno=sno).first()
          post.title = box_title
          post.tagline = tline
          post.slug = slug
          post.content = content
          post.img_file = img_file
          try:
              db.session.commit()
          except:
              flash('title should be unique')
          return redirect(url_for('posts.edit',sno=sno))
  post = Posts.query.filter_by(sno=sno).first()
  return render_template('edit.html', params=params, post=post, sno=sno)


@posts_blueprint.route("/uploader", methods=["GET", "POST"])
def uploader():
    if (request.method == 'POST'):
        f = request.files['file1']
        f.save(os.path.join(app.config['UPLOAD_FOLDER']))#, secure_filename(f.filename)))
        return "Uploaded successfully"

@posts_blueprint.route("/delete/<string:sno>", methods=["GET", "POST"])
def delete(sno):
    post = Posts.query.filter_by(sno=sno).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/dashboard')
