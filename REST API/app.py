from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Silence'

@app.route('/hello')
def hello():
    return 'Hello!'

@app.route('/helloX')

@app.route('/helloY')

def hello_both():
    return 'Hello everyone!'

app.add_url_rule('/helloX', '/helloY', hello_both)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello ' + name + '!'

@app.route('/hello/<int:number>')
def hello_number(number):
    return 'Hello ' + str(number+1) + '!'

@app.route('/url')
def get_main_url():
    return url_for('index')

@app.route('/seznam')
def go_to_seznam():
    return redirect('http://www.seznam.cz')

@app.route('/me')
def hello_me():
    return redirect(url_for('hello_name', name='Tom'))

@app.route('/nice_hello')
def nice_hello():
    #return "<html><body><h1>Hello world!</h1></body></html>"
    return render_template('hello.html')

@app.route('/nice_hello/<user>')
def nice_hello_user(user):
    return render_template('hello_name.html', name=user)

app.run()
