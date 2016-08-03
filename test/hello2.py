#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, url_for, request, render_template 

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello, Welcome to python world!'

@app.route('/hello')
@app.route('/hello/<username>')
def hello(username=None):
	return render_template('hello.html', name=username)

@app.route('/user/<username>')
def user(username):
	return 'hello, %s' % username

#with app.test_request_context():
#	print(url_for('index'))
#	print(url_for('login'))
#	print(url_for('login', next='/'))
#	print(url_for('user', username='pizhuaizhuai'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return show_login_form()
	else:
		return do_login()

def show_login_form():
	return 'hello, please login!'

def do_login():
	return 'hello, welcome back!'

@app.route('/file', methods=['GET', 'POST'])
def file():
	if request.method == 'POST':
		f = request.files['file']
		f.save('/data/wwwroot/python-projects/awesome-python-app/uploads/a.txt')
		return 'upload success!'
	else:
		return render_template('file.html')

if __name__ == '__main__':
	app.run()
