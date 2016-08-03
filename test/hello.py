#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'It works!'

@app.route('/hello')
def hello():
	return 'hello, world!'

@app.route('/user/<username>')
def user_profile(username):
	return 'hello, %s' % username

@app.route('/post/<int:post_id>')
def post(post_id):
	return 'post id is %d' % post_id

if __name__ == '__main__':
	app.run(debug=True)

