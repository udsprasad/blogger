# contact views

from project import db,mail,params
from flask import Blueprint,render_template,request
from project.contacts.models import Contacts
from datetime import datetime

contacts_blueprint=Blueprint('contacts',__name__,template_folder='templates/contacts')

@contacts_blueprint.route("/add_contact", methods= ['GET', 'POST'])

def contact():
    if (request.method=='POST'):
        "Add entry to db"
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message= request.form.get('message')
        # sno , name , email , phone_no , msg , date #db variables
        entry = Contacts(name=name, phone_no=phone, email=email, date=datetime.now(), msg=message)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('Message from Blogger.com' + name,
                          sender=email,
                          recipients= [params['gmail_user']],
                          body= message + "\n" + phone
                          )
    return render_template("contact.html", params=params)
