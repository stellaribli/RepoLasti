from flask import Flask, render_template, request, request, redirect, url_for
from werkzeug.utils import secure_filename 
import os

app = Flask(__name__)
@app.route('/')


@app.route('/pilih')
def pilih():
    return render_template('pilih.html')

@app.route('/PM')
def pm():
    name = 'Calon PM'
    nilai = 122

    # Untuk Keywords bagian tengah 
    textkeywords = ''
    arraykeywords = ['Kalimat satu','Kalimat lalalala b']
    for i in range (len(arraykeywords)):
        textkeywords = textkeywords + ' ' + (arraykeywords[i])

    # Untuk Tips bagian kanan
    textsaran = ''
    arrayksaran = ['aaasdfa','bdfafad']
    for i in range (len(arrayksaran)):
        textsaran = textsaran + ' ' + (arrayksaran[i])

    return render_template('index.html', username=name, keywords = textkeywords, saran = textsaran, cvscore = nilai)



@app.route('/SE')
def se():
    name = 'Calon SE'
    nilai = 122

    # Untuk Keywords bagian tengah 
    textkeywords = ''
    arraykeywords = ['Kalimat satu','Kalimat lalalala b']
    for i in range (len(arraykeywords)):
        textkeywords = textkeywords + ' ' + (arraykeywords[i])

    # Untuk Tips bagian kanan
    textsaran = ''
    arrayksaran = ['aaasdfa','bdfafad']
    for i in range (len(arrayksaran)):
        textsaran = textsaran + ' ' + (arrayksaran[i])

    return render_template('index.html', username=name, keywords = textkeywords, saran = textsaran, cvscore = nilai)



@app.route('/Finance')
def fin():
    name = 'Calon Finance bitj'
    nilai = 122

    # Untuk Keywords bagian tengah 
    textkeywords = ''
    arraykeywords = ['Kalimat satu','Kalimat lalalala b']
    for i in range (len(arraykeywords)):
        textkeywords = textkeywords + ' ' + (arraykeywords[i])

    # Untuk Tips bagian kanan
    textsaran = ''
    arrayksaran = ['aaasdfa','bdfafad']
    for i in range (len(arrayksaran)):
        textsaran = textsaran + ' ' + (arrayksaran[i])

    return render_template('index.html', username=name, keywords = textkeywords, saran = textsaran, cvscore = nilai)


@app.route('/Designer')
def des():
    name = 'Calon Designer apalah'
    nilai = 122

    # Untuk Keywords bagian tengah 
    textkeywords = ''
    arraykeywords = ['Kalimat satu','Kalimat lalalala b']
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
        return redirect(url_for('pm'))
    return render_template('upload.html')

app.run(host='0.0.0.0', port=80)