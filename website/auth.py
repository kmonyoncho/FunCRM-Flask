from flask import Blueprint, render_template, request, flash, redirect, url_for, session

from website.forms import LoginForm, UserRegistrationForm
from .models import fs_acuserprofiles
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = fs_acuserprofiles.query.filter_by(UserName=form.username.data).first()
        if user:
            if check_password_hash(user.PasswordHash, form.password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=form.remember.data)   
                next_page = request.args.get('next')             
                return redirect(next_page) if next_page else redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again!', category='error')
        else:
            flash('Username does not exist.', category='error')

    return render_template("login.html", next=request.url,user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':        

        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form = UserRegistrationForm()  
        if form.validate_on_submit():
            new_user = fs_acuserprofiles(EmployeeId=2, Email=form.email.data, FirstName=form.firstname.data, LastName=form.lastname.data, UserName=form.username.data, PhoneNumber=form.phonenumber.data, PasswordHash=generate_password_hash(
                form.password.data, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created Successfully!', category='success')
            return redirect(url_for('login'))

    return render_template("register.html", title='User Register', form=form, user=current_user)
