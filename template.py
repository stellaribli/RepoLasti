from flask import Flask, render_template, request, request, redirect, url_for
from werkzeug.utils import secure_filename 
import os

app = Flask(__name__)
x=12
@app.route('/')
@app.route('/index')
def index():
    name = 'StelalCantik'
    nilai = 122
    textkeywords = 'Saran gue sich lo mending pake keyword a, b, c ye'
    textsaran = 'Iuh jelek CVnya'
    return render_template('index.html', username=name, keywords = textkeywords, saran = textsaran, cvscore = nilai)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('index'))
    return render_template('upload.html')

app.run(host='0.0.0.0', port=80)