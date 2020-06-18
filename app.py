from project import app,db
from flask import render_template,request
from project.posts.models import Posts

@app.route('/')
def home():
    posts = Posts.query.all() #[0:params['no_of_posts']]
    return render_template('index.html', params=params, posts=posts)

@app.route("/dashboard", methods=['GET','POST'])
def dashboard():

    if ('user' in session and session['user'] == params['admin-user']):
        posts = Posts.query.all()
        return render_template('dashboard.html',params=params, posts=posts)
    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username==params['admin-user'] and userpass==params['admin-pass']):
            # setting session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html',params=params, posts=posts)
    return render_template("login.html", params=params)

@app.route("/about")
def about():
    return render_template("about.html", params=params)


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')

if __name__=='__main__':
    app.run(debug=True)
