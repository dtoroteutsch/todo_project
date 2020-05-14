from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/hello')
def hello():
    return 'Hello world - Flask'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
