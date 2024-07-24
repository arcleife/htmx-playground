from flask import Flask, render_template

server = Flask(__name__)

@server.route('/')
def root():
    return render_template('index.html')

@server.route('/test')
def test():
    return render_template('test.html')