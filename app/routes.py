from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('home.html')


#### Albums
@app.route('/albums')
@app.route('/albums/show')
def show_albums():
    return render_template('albums/show.html')

@app.route('/albums/create')
def new_album():
    return render_template('albums/create.html')

@app.route('/albums/update')
def update_album():
    return render_template('albums/update.html')

@app.route('/albums/delete')
def delete_album():
    return render_template('albums/show.html')