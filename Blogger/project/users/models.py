from project import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from project.like.models import Like

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(10),nullable=False,unique=True)
    email=db.Column(db.String(20),nullable=False,unique=True)
    password_hash=db.Column(db.String(128),nullable=False)
    posts=db.relationship("Posts",backref='owner')
    liked=db.relationship('Like',backref='user',lazy='dynamic', foreign_keys='Like.liked_id')

    def __init__(self,email,username,password_hash):
        self.username=username
        self.email=email
        self.password_hash=generate_password_hash(password_hash)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)


    def like_post(self,post):
        if not self.has_liked_post(post):
            db.session.add(Like(liked_id=self.id,post_id=post.sno))
            db.session.commit()

    def unlike_post(self,post):
        if self.has_liked_post(post):
            Like.query.filter_by(liked_id=self.id,post_id=post.sno).delete()

    def has_liked_post(self,post):
        return Like.query.filter_by(liked_id=self.id,post_id=post.sno).count() > 0
