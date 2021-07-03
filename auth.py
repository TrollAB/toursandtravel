from flask import Blueprint,render_template, request , flash
from flask.helpers import url_for
from werkzeug.utils import redirect
from . import db
from .models import User
from werkzeug.security import check_password_hash, generate_password_hash
auth = Blueprint('auth' , __name__)

@auth.route('/login' ,methods = ['GET' , 'POST'])
def login():
    if request.method == "POST":
        Email  = request.form.get('email')
        password = request.form.get("Password")
        print(f"{Email } {password}")
        user = User.query.filter_by(email = Email).first()
        print(user)
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category= 'success')
                return redirect(url_for('views.Home'))
            else:
                flash('password incorrect ', category= 'error')
        else:
            flash('email already exist', category='error')


    return render_template('login.html' )



@auth.route('/signup',methods = ['GET' , "POST"])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password = request.form.get('Password')
        password2 = request.form.get('Password2')
        # print(f'{password}  {password2}')
        user = User.query.filter_by(email = email).first()
        if user:
            flash("email already exist" ,category= 'error')

        elif len(email)  < 2:
            flash("email must be greater than 2 charaters ", category="error")
        elif len(password) < 8 or len(password) >16:
            flash('password must be greater than 8 characters and less than 16 charcters ', category="error")
       
        elif password != password2:
            flash("password doesn't match ", category= "error")
       
        else:
            new_user = User(email = email, firstname = firstname, password = generate_password_hash(password , method ='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Successfully created ', category= 'success')
            return redirect(url_for('views.Home'))


    return render_template('signup.html')

