from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Its a beautiful morning'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Love me some deathcore in the morning'
        },
        {
            'author': {'username': 'Rodrigo'},
            'body': 'I think i caught the pox'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)
