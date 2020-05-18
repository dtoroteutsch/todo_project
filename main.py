from flask import request, make_response, redirect
from flask import render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
import unittest

from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['Buy coffee', 'Study Flask', 'Eat many things']

@app.cli.command()
def test():
    tests =  unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')

    context = {
        'title': 'Hello',
        'user_ip': user_ip,
        'todos': todos,
        'username': username
    }

    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
