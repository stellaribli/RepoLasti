from flask import Flask, render_template, request, request, redirect, url_for
from werkzeug.utils import secure_filename 
import os

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    name = 'StelalCantik'
    nilai = 122

    # Untuk Keywords bagian tengah 
    textkeywords = ''
    arraykeywords = ['aa','b']
    for i in range (len(arraykeywords)):
        textkeywords = textkeywords + ' ' + (arraykeywords[i])

    # Untuk Tips bagian kanan
    textsaran = ''
    arrayksaran = ['aaasdfa','bdfafad']
    for i in range (len(arrayksaran)):
        textsaran = textsaran + ' ' + (arrayksaran[i])

    return render_template('index.html', username=name, keywords = textkeywords, saran = textsaran, cvscore = nilai)

namafilecv = ""
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        namafilecv = uploaded_file.filename
        return redirect(url_for('index'))
    return render_template('upload.html')

app.run(host='0.0.0.0', port=80)