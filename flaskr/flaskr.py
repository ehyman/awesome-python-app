#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sqlite3, os
from flask import Flask, url_for, render_template, request, \
				  session, g, abort, flash, redirect

from contextlib import closing

#configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECURE_KEY = os.urandom(24)
USERNAME = 'root'
PASSWORD = '123456'

#create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.before_request
def before_request():
	g.db = connect_db()

@qpp.teardown_request
def teardown_request(exception):
	g.db.close()

if __name__ == '__main__':
	app.run()

