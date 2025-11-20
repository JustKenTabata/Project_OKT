import os
from flask import Blueprint, render_template, request, redirect, url_for,  current_app, flash
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
from . import db
from .models import Video, User

main = Blueprint('main', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        

        if User.query.filter_by(email=email).first():
            flash('Email already exists.')
            return redirect(url_for('main.register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('main.login'))
    
    return render_template('register.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print("POST data:", email, password)

        user = User.query.filter_by(email=email).first()

        if user:
            check = user.check_password(password)
        else:
            print("User not found")

        if user and user.check_password(password):
            login_user(user)
            print(" current_user.is_authenticated:", current_user.is_authenticated)
            flash('Logged in successfully!')
            return redirect(url_for('main.diary'))
        else:
            flash('Invalid credentials')
            print("Login failed")

    return render_template('login.html')


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))



@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        if 'video' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['video']
        description = request.form.get('description')
        if file.filename == '':
            flash('No seleceted file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename).lower()
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            print("app.root_path =", current_app.root_path)
            print("UPLOAD_FOLDER =", current_app.config['UPLOAD_FOLDER'])
            file.save(upload_path)
            
            new_video = Video(filename=filename, description=description)
            db.session.add(new_video)
            db.session.commit()

            flash('Upload Successful!')
            return redirect(url_for('main.upload', filename=filename))
    filename = request.args.get('filename')
    description = None
    if filename:
        video = Video.query.filter_by(filename=filename).first()
        if video:
            description = video.description

    return render_template('upload.html', video_filename=filename, description=description)


@main.route('/diary')
def diary():
    videos = Video.query.order_by(Video.timestamp.desc()).all()
    return render_template('diary.html', videos=videos)
