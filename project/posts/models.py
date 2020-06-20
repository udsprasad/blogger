# posts models


from project import db

class Posts(db.Model):
    # sno , name , email , phone_no , msg , date #db variables
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),unique=True, nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(400), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_name = db.Column(db.String(20), nullable=True)
    owner_id=db.Column(db.Integer,db.ForeignKey('user.id'))
