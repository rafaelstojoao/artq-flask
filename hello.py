from flask import Flask, url_for
from flask import render_template



app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, world!'

@app.route('/hello')
def hello2():
	return 'Nova página!'

@app.route('/pagina/<nome>')
def pagNome(nome):
	return 'Ola %s' %nome

@app.route('/hello/')
@app.route('/hello/<name>')
def hello3(name=None):
	return render_template('hello.html', name=name)

