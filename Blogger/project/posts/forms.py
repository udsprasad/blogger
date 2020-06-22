from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField,TextAreaField,ValidationError
from wtforms.validators import DataRequired,Length
from flask_wtf.file import FileAllowed
from project.posts.models import Posts

class Addform(FlaskForm):

    title=StringField('Title',validators=[DataRequired(message='Input Required')])
    tagline=StringField('Tagline',validators=[DataRequired(message='Input Required')])
    slug=StringField('Slug',validators=[DataRequired(message='Input Required')])
    content=TextAreaField('Content',validators=[DataRequired(message='Input Required'),Length(min=10,message='atleast 10 Characters')])
    image=FileField('Upload image',validators=[FileAllowed([ 'png', 'jpg', 'jpeg', 'gif'],message='formats allowed png,jpg ,jpeg,gif')])
    submit=SubmitField('Submit')

    def validate_title(self,title):
        if Posts.query.filter_by(title=self.title.data).first():
            raise ValidationError('Title has already present')

    def validate_slug(self,slug):
        if Posts.query.filter_by(slug=self.slug.data).first():
            raise ValidationError('Slug has already present')
