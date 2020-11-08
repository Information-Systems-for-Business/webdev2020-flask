from flask import Flask, render_template, url_for
from app import app
from app.models.user import User ## import kelas User dari model

@app.route('/', methods = ['GET'])
def index():
	user =  User() ## membuat objek dari kelas user
	nama = user.getName() ## memanggil method untuk mengambil nama
	return render_template('index.html', nama=nama)