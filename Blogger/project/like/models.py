from project import db

class Like(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    liked_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    post_id=db.Column(db.Integer,db.ForeignKey('posts.sno'))
