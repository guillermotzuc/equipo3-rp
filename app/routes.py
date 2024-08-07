import os
import uuid
from flask import Flask, flash, request, redirect, render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'Miguel' }
    posts = [
        {
            'author' : { 'username' : 'John'},
            'body' : 'Beautiful day in Portland!'
        },
        {
            'author' : { 'username' : 'Susan'},
            'body' : 'The Avengers movie was so cool!'           
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/save-record', methods=['POST'])
def save_record():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    file_name = str(uuid.uuid4()) + ".mp3"
    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(full_file_name)
    return render_template('index.html', title ='Home')

