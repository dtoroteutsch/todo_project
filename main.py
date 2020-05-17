from flask import Flask, request, make_response, redirect
from flask import render_template, session, url_for, flash
from flask_bootstrap import Bootstrap

from forms import LoginForm

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = '1Nw4rdH33lfl1p'

todos = ['Buy coffee', 'Study Flask', 'Eat many things']

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
    login_form = LoginForm()
    username = session.get('username')

    context = {
        'title': 'Hello',
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('User logged successfully')
        return redirect(url_for('index'))

    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
