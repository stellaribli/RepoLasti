from flask import Flask, render_template

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename 
import os
app = Flask(__name__)

ALLOWED_EXTENSION = set(['png', 'jpeg', 'jpg','pdf'app.config['UPLOAD_FOLDER'] = 'uploads'

#pengecekan file degan menggunakan rsplit
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION
   
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        file = request.files['file']

        if 'file' not in request.files:
            return render_template('upload.html')

        if file.filename == '':
            return render_template('upload.html')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],  filename))            return  'file ' + filename +' di simpan' + ' <a href="/upload">kembali</a>'

    return render_template('upload.html')

app.run(debug=True)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename 
import os
app = Flask(__name__)

x=12
@app.route('/')
@app.route('/index')
def index():
    name = 'StelalCantik'
    nilai = 12
    textkeywords = 'Saran gue sich lo mending pake keyword a, b, c ye'
    textsaran = 'Iuh jelek CVnya'
    return render_template('index.html', username=name, keywords = textkeywords, saran = textsaran, cvscore = nilai)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
 
        file = request.files['file']
 
        if 'file' not in request.files:
            return render_template('upload.html')
 
        if file.filename == '':
            return render_template('upload.html')
 
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],  filename))            return  'file ' + filename +' di simpan' + ' <a href="/upload">kembali</a>'
 
    return render_template('upload.html')

app.run(host='0.0.0.0', port=80)