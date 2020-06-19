from project import app,db,params
from flask import render_template,request,session,redirect,flash,url_for
from project.posts.models import Posts
from project.users.models import User
from flask_login import login_user,login_required,logout_user

@app.route('/')
def index():
    posts = Posts.query.all()
    users=User.query.all()
    return render_template('index.html', params=params, posts=posts,users=users)

@app.route("/dashboard/<user_id>")
@login_required
def dashboard(user_id):
    posts = Posts.query.filter_by(owner_id=user_id)
    return render_template('dashboard.html',params=params, posts=posts,user_id=user_id)

@app.route("/about")
def about():
    return render_template("about.html", params=params)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user= User.query.filter_by(email=request.form.get('email')).first()
        if user is not None and user.check_password(request.form.get('password')):
            login_user(user)
            user_id=user.id
            next=request.args.get('next')
            if next==None or not next[0]=='/':
                 next=url_for('dashboard',user_id=user_id)
            return redirect(next)
    return render_template('login.html',params=params)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you logged out')
    return render_template('index.html',params=params)


if __name__=='__main__':
    app.run(debug=True)
