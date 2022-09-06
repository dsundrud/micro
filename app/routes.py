from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David'}
    posts = [
        {
            'author': {'username': 'Ivan'},
            'body': 'Anybody want some coffee?'
        },
        {
            'author': {'username': 'Ralph'},
            'body': 'JUST AS GOOD!'
        },
        {
            'author': {'username': 'Carlos'},
            'body': 'I GOT BIT!!!'
        },
        {
            'author': {'username': 'Adam'},
            'body': 'STOP!'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
