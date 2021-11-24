from flask import Flask, render_template, request, request, redirect, url_for
from werkzeug.utils import secure_filename 
import os
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
@app.route('/')
def pilihawal():
    return render_template('pilih.html')

 ##############PAGE PILIH ROLE#####################
 ##################################################
 ##################################################
@app.route('/pilih')
def pilih():
    file = open("CV.txt","r+")
    file. truncate(0)
    os.remove("CV.jpg") 
    return render_template('pilih.html')

 ##############PAGE PM#############################
 ##################################################
 ##################################################
cvPM = ""
@app.route('/uploadPM', methods=['GET', 'POST'])
def uploadPM():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        cvPM = uploaded_file.filename
        return redirect(url_for('pm'))
    return render_template('upload.html')

@app.route('/PM')
def pm():
    peran = 'Product Manager'
    name = 'Akselzen'
    nilai = 25
    textkeywords = "Berikut keyword yang bisa kamu pakai!\n"
    textsaran = " "

    #####CONVERT
    img = cv2.imread('CV.jpg')
    txt = pytesseract.image_to_string(img)
    
    file = open('CV.txt', 'w')
    file.write(txt)
    file.close()

    #BASEDONROLES1 [10%]
    def check():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Administered' in line:
                return True
        return False 

    if check():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Administered-\n'

    #BASEDONROLES2 [10%]
    def check2():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Managed' in line:
                return True
        return False 

    if check2():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Managed-\n'

    #BASEDONROLES3 [10%]
    def check3():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Produced' in line:
                return True
        return False 

    if check3():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Produced-\n'

    #BASEDONROLES4 [10%]
    def check4():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Organized' in line:
                return True
        return False 

    if check4():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Organized-\n'

    #BASEDONROLES5 [10%]
    def check5():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Executed' in line:
                return True
        return False 

    if check5():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Executed-\n'

    #BASEDONROLES6 [10%]
    def check6():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Prioritized' in line:
                return True
        return False 

    if check6():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Prioritized-\n'

    #BASEDONROLES7 [10%]
    def check7():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Supervised' in line:
                return True
        return False 

    if check7():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Supervised-\n'

    #BASEDONROLES8 [10%]
    def check8():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Reviewed' in line:
                return True
        return False 

    if check8():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Reviewed-\n'

    #BASEDONROLES9 [10%]
    def check9():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Product Manager' in line:
                return True
        return False 

    if check9():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Product Manager-\n'


    #BASEDONROLES10 [10%]
    def check10():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Product' in line:
                return True
        return False 

    if check10():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Product-\n'

    #GAADA LINKEDIN [-10%]
    def check11():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'linkedin' in line:
                return True
        return False 

    if check11():
        nilai == nilai
        textsaran += 'Perbanyak penggunaan keyword yap!'
    else:
        nilai -= 10
        textsaran += 'Sertakan akun linkedin. '

    #GAADA NOTELP [-10%]
    def check12():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if '+62' in line:
                return True
        return False 

    if check12():
        nilai == nilai
        textsaran += 'Perbanyak penggunaan keyword yap!'
    else:
        nilai -= 10
        textsaran += 'Sertakan nomor telepon kamu.'
    
    return render_template('index.html', role = peran, username=name, keywords = textkeywords, saran = textsaran, cvscore = nilai)

 ##############PAGE SOFTENG#############################
 ##################################################
 ##################################################
cvSE = ""
@app.route('/uploadSE', methods=['GET', 'POST'])
def uploadSE():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        cvSE = uploaded_file.filename
        return redirect(url_for('se'))
    return render_template('upload.html')

@app.route('/SE')
def se():
    peran = 'Software Engineer'
    name = 'Akselzen'
    nilai = 25
    textkeywords = "Berikut keyword yang bisa kamu pakai!\n"
    textsaran = ""

    #####CONVERT
    img = cv2.imread('CV.jpg')
    txt = pytesseract.image_to_string(img)
    
    file = open('CV.txt', 'w')
    file.write(txt)
    file.close()

    #BASEDONROLES1 [10%]
    def check():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Software Engineer' in line:
                return True
        return False 

    if check():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Software Engineer-\n'

    #BASEDONROLES2 [10%]
    def check2():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Installed' in line:
                return True
        return False 

    if check2():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Installed-\n'

    #BASEDONROLES3 [10%]
    def check3():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Debugged' in line:
                return True
        return False 

    if check3():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Debugged-\n'

    #BASEDONROLES4 [10%]
    def check4():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Predicted' in line:
                return True
        return False 

    if check4():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Predicted-\n'

    #BASEDONROLES5 [10%]
    def check5():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Deployed' in line:
                return True
        return False 

    if check5():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Deployed-\n'

    #BASEDONROLES6 [10%]
    def check6():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Automated' in line:
                return True
        return False 

    if check6():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Automated-\n'

    #BASEDONROLES7 [10%]
    def check7():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Troubleshooted' in line:
                return True
        return False 

    if check7():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Troubleshooted-\n'

    #BASEDONROLES8 [10%]
    def check8():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Conceptualized' in line:
                return True
        return False 

    if check8():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Conceptualized-\n'

    #BASEDONROLES9 [10%]
    def check9():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Tested' in line:
                return True
        return False 

    if check9():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Tested-\n'


    #BASEDONROLES10 [10%]
    def check10():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Assembled' in line:
                return True
        return False 

    if check10():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Assembled-\n'

    #GAADA LINKEDIN [-10%]
    def check11():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'linkedin' in line:
                return True
        return False 

    if check11():
        nilai == nilai
        textsaran += 'Perbanyak penggunaan keyword yap!'
    else:
        nilai -= 10
        textsaran += 'Sertakan akun linkedin. '

    #GAADA NOTELP [-10%]
    def check12():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if '+62' in line:
                return True
        return False 

    if check12():
        nilai == nilai
        textsaran += 'Perbanyak penggunaan keyword yap!'
    else:
        nilai -= 10
        textsaran += 'Sertakan nomor telepon kamu.'
    
    return render_template('index.html', role = peran, username=name, keywords = textkeywords, saran = textsaran, cvscore = nilai)

 ##############PAGE GRAPHIC DESIGN#################
 ##################################################
 ##################################################
cvGD = ""
@app.route('/uploadGD', methods=['GET', 'POST'])
def uploadGD():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        cvGD = uploaded_file.filename
        return redirect(url_for('gd'))
    return render_template('upload.html')

@app.route('/GD')
def gd():
    peran = 'Graphic Designer'
    name = 'Akselzen'
    nilai = 25
    textkeywords = "Berikut keyword yang bisa kamu pakai!\n"
    textsaran = ""

    #####CONVERT
    img = cv2.imread('CV.jpg')
    txt = pytesseract.image_to_string(img)
    
    file = open('CV.txt', 'w')
    file.write(txt)
    file.close()

    #BASEDONROLES1 [10%]
    def check():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Graphic Designer' in line:
                return True
        return False 

    if check():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Graphic Designer-\n'

    #BASEDONROLES2 [10%]
    def check2():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Conceptualized' in line:
                return True
        return False 

    if check2():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Conceptualized-\n'

    #BASEDONROLES3 [10%]
    def check3():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Illustrated' in line:
                return True
        return False 

    if check3():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Illustrated-\n'

    #BASEDONROLES4 [10%]
    def check4():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Designed' in line:
                return True
        return False 

    if check4():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Designed-\n'

    #BASEDONROLES5 [10%]
    def check5():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Proved' in line:
                return True
        return False 

    if check5():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Proved-\n'

    #BASEDONROLES6 [10%]
    def check6():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Redesigned' in line:
                return True
        return False 

    if check6():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Redesigned-\n'

    #BASEDONROLES7 [10%]
    def check7():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Established' in line:
                return True
        return False 

    if check7():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Established-\n'

    #BASEDONROLES8 [10%]
    def check8():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Planned' in line:
                return True
        return False 

    if check8():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Planned-\n'

    #BASEDONROLES9 [10%]
    def check9():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Validated' in line:
                return True
        return False 

    if check9():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Validated-\n'


    #BASEDONROLES10 [10%]
    def check10():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Tabulated' in line:
                return True
        return False 

    if check10():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Tabulated-\n'

    #GAADA LINKEDIN [-10%]
    def check11():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'linkedin' in line:
                return True
        return False 

    if check11():
        nilai == nilai
        textsaran += 'Perbanyak penggunaan keyword yap!'
    else:
        nilai -= 10
        textsaran += 'Sertakan akun linkedin. '

    #GAADA NOTELP [-10%]
    def check12():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if '+62' in line:
                return True
        return False 

    if check12():
        nilai == nilai
        textsaran += 'Perbanyak penggunaan keyword yap!'
    else:
        nilai -= 10
        textsaran += 'Sertakan nomor telepon kamu.'
    
    return render_template('index.html', role = peran, username=name, keywords = textkeywords, saran = textsaran, cvscore = nilai)

##############PAGE FINANCE#########################
 ##################################################
 ##################################################
cvF = ""
@app.route('/uploadF', methods=['GET', 'POST'])
def uploadF():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        cvF = uploaded_file.filename
        return redirect(url_for('fin'))
    return render_template('upload.html')

@app.route('/Finance')
def fin():
    peran = 'Finance'
    name = 'Akselzen'
    nilai = 25
    textkeywords = "Berikut keyword yang bisa kamu pakai!\n"
    textsaran = ""

    #####CONVERT
    img = cv2.imread('CV.jpg')
    txt = pytesseract.image_to_string(img)
    
    file = open('CV.txt', 'w')
    file.write(txt)
    file.close()

    #BASEDONROLES1 [10%]
    def check():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Finance' in line:
                return True
        return False 

    if check():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Finance-\n'

    #BASEDONROLES2 [10%]
    def check2():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Administered' in line:
                return True
        return False 

    if check2():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Administered-\n'

    #BASEDONROLES3 [10%]
    def check3():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Calculated' in line:
                return True
        return False 

    if check3():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Calculated-\n'

    #BASEDONROLES4 [10%]
    def check4():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Audited' in line:
                return True
        return False 

    if check4():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Audited-\n'

    #BASEDONROLES5 [10%]
    def check5():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Projected' in line:
                return True
        return False 

    if check5():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Projected-\n'

    #BASEDONROLES6 [10%]
    def check6():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Budgeted' in line:
                return True
        return False 

    if check6():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Budgeted-\n'

    #BASEDONROLES7 [10%]
    def check7():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Balanced' in line:
                return True
        return False 

    if check7():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Balanced-\n'

    #BASEDONROLES8 [10%]
    def check8():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Allocated' in line:
                return True
        return False 

    if check8():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Allocated-\n'

    #BASEDONROLES9 [10%]
    def check9():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Developed' in line:
                return True
        return False 

    if check9():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Developed-\n'


    #BASEDONROLES10 [10%]
    def check10():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'Managed' in line:
                return True
        return False 

    if check10():
        nilai += 10
    else:
        nilai == nilai
        textkeywords += '-Managed-\n'

    #GAADA LINKEDIN [-10%]
    def check11():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if 'linkedin' in line:
                return True
        return False 

    if check11():
        nilai == nilai
        textsaran += 'Perbanyak penggunaan keyword yap!'
    else:
        nilai -= 10
        textsaran += 'Sertakan akun linkedin. '

    #GAADA NOTELP [-10%]
    def check12():
        with open('CV.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if '+62' in line:
                return True
        return False 

    if check12():
        nilai == nilai
        textsaran += 'Perbanyak penggunaan keyword yap!'
    else:
        nilai -= 10
        textsaran += 'Sertakan nomor telepon kamu.'
    
    return render_template('index.html', role = peran, username=name, keywords = textkeywords, saran = textsaran, cvscore = nilai)

app.run(host='0.0.0.0', port=80)