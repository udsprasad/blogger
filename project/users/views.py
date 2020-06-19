from flask import Blueprint,request,render_template,redirect,url_for,flash
from project.users.models import User
from project import db
from project.users.forms import Registerform

user_blueprint=Blueprint('user',__name__,template_folder='templates/users')

@user_blueprint.route('/register',methods=['GET','POST'])
def register():
     form=Registerform()
     if form.validate_on_submit():
         user=User(form.email.data,form.username.data,form.password.data)
         db.session.add(user)
         db.session.commit()
         flash('Successfully registered')
         return redirect(url_for('user.login'))
     return render_template('register.html',form=form)
