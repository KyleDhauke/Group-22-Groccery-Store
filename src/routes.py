from src import app, db
from flask import render_template, url_for, abort, request, redirect, flash, session, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from src.models import User,List,lists_landmarks,Landmark
from src.forms import RegistrationForm, ReviewForm, LoginForm, CreatelistForm, MarkerInfo, ChangeusernameForm, ChangeemailForm, ChangepasswordForm 
from werkzeug.utils import secure_filename
import os
import time
from random import seed, randint, choice
from src.email import send_email

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    #seed(int(round(time.time() * 1000)))
    form = MarkerInfo()
    lists = List.query.order_by(List.name)
    all_markers = Landmark.query.all()
    if(current_user.is_authenticated):
        for o in all_markers:
            for x in all_markers:
                if x.userid != current_user.id:
                    all_markers.remove(x)
    print(type(all_markers))
    if (form.validate_on_submit()):
        landmark = Landmark(name=form.name.data, description=form.description.data, 
        tags=form.tags.data, lat=form.lat.data, lng=form.lng.data, userid=current_user.id)
        db.session.add(landmark)
        db.session.commit()
    return render_template('home.html', lists=lists, form=form, all_markers=all_markers)
    #, form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = LoginForm()
    if (form.validate_on_submit()):
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(password=form.password.data):
            login_user(user)
            if user.confirmed == 1:
                return redirect(url_for('home'))
            else:
                flash("Please confirm your email address", category='bad')
        else:
            flash("Login unsuccessful! Invalid username or password.", category='bad')
    return render_template('login.html', title='Sign In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account',
                   'auth/confirm',user=user,token=token)
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)

@app.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('home'))
    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('home'))

@app.route("/accountDetails", methods=['GET', 'POST'])
def accountDetails():
    # form = AccountDetailsForm()
    lists = List.query.all()
    # if form.validate_on_submit():
    #     user = User(username=form.name.data, email=form.email.data, password=form.password.data)
    #     db.session.add(user)
    #     db.session.commit()
    #     return redirect(url_for('accountDetails'))
    return render_template('accountDetails.html', title='accountDetails', lists=lists)


@app.route("/lists")
def lists():
    lists = List.query.all()
    return render_template('lists.html', title='Lists',lists = lists)

@app.route("/creatlists", methods=['GET', 'POST'])
def createlists():
    form = CreatelistForm()
    if (form.validate_on_submit()):
        list = List(name=form.listname.data,userid = current_user.id)
        db.session.add(list)
        db.session.commit()
        return redirect(url_for("lists"))
    return render_template('createlists.html', title='Createlists',form = form)

@app.route("/landmarks/<listid>")
def landmarks(listid):
    #All the landmarks in a list of list_landmarks table
    landmarks_data_id = lists_landmarks.query.filter(lists_landmarks.listid == listid).all()
    #All the landmarks from that list
    landmarks_data = []
    for i in range(len(landmarks_data_id)):
        landmarks_data.extend(Landmark.query.filter(Landmark.landmarkid == landmarks_data_id[i].landmarkid,Landmark.userid == current_user.id).all())
    return render_template('landmark.html',landmarks_data = landmarks_data)

@app.route("/change_username", methods=['GET','POST'])
def change_username():
    form = ChangeusernameForm()
    if (form.validate_on_submit()):
        user = User.query.get(current_user.id)
        user.username= form.username.data
        db.session.commit()
        return redirect(url_for("accountDetails"))
    return render_template('changeusername.html',title='ChangeUsername',form=form)

@app.route("/change_email", methods=['GET','POST'])
def change_email():
    form = ChangeemailForm()
    if (form.validate_on_submit()):
        user = User.query.get(current_user.id)
        user.email= form.email.data
        db.session.commit()
        return redirect(url_for("accountDetails"))
    return render_template('changeemail.html',title='ChangeEmail',form=form)

@app.route("/change_password", methods=['GET','POST'])
def change_password():
    form = ChangepasswordForm()
    if (form.validate_on_submit()):
        user = User.query.get(current_user.id)
        user.password= form.password.data
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('changepassword.html',title='ChangePassword',form=form)

SUPPORTED_IMG_TYPES = {"png", "bmp", "svg"}

def get_file_ext(filename):
    return filename.rsplit('.', 1)[1].lower() if '.' in filename else '';

def image_ext_error():
    flash("Invalid image file format! Supported file types: " + str(SUPPORTED_IMG_TYPES).strip()[1:-1], category='bad')
