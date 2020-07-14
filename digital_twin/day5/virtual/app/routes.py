from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    data = {'firm':'toshiba'}
    user = {'username':'tsip-admin'}
    return render_template('index.html', title='Home', user=user, data=data)

@app.route('/display')
def display():
    data = {'firm':'toshiba'}
    value = 100
    user = {'username':'tsip-admin'}
    info = [
            {'name':'tsip','username':'tsip-admin'},
            {'name':'john', 'username':'johndoe'},
            {'name':'jane', 'username':'janedoe'},
            ]
    return render_template('display.html', info=info, data=data)


