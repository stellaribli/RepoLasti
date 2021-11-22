from flask import Flask, render_template

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

@app.route('/revisi/')
def indexx():
    name = 'StelalCantik'
    nilaicv = 12
    textkeywords = 'Sekarang lo jelek'
    textsaran = 'Iuh jelek CVnya'
    return render_template('index.html', username=name, keywords = textkeywords, saran = textsaran, cvscore = nilaicv)



app.run(host='0.0.0.0', port=80)