# routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request  
from flask_login import login_user, login_required, logout_user, current_user
from forms import PredictionForm
from models import db, User
from predict_model import make_prediction

index = Blueprint('index', __name__)
auth = Blueprint('auth', __name__)
predict = Blueprint('predict', __name__)

@index.route('/')
def home():
    return render_template('index.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@predict.route('/predict', methods=['GET', 'POST'])
@login_required
def predict_wine():
    form = PredictionForm()

    if form.validate_on_submit():
        features = [
            form.fixed_acidity.data,
            form.volatile_acidity.data,
            form.citric_acid.data,
            form.residual_sugar.data,
            form.chlorides.data,
            form.free_sulfur_dioxide.data,
            form.total_sulfur_dioxide.data,
            form.density.data,
            form.pH.data,
            form.sulphates.data,
            form.alcohol.data
        ]

        output = make_prediction(features)

        return render_template('index.html', form=form, prediction_text=f'Predicted output: {output}')

    return render_template('index.html', form=form)
