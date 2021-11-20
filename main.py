# import pytesseract
# import cv2

# #ini buat convert dari jpg ke txt duls
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# img = cv2.imread('CV Rahmat Fabhian A_page-0001.jpg')
# img2 = cv2.imread('CV Rahmat Fabhian A_page-0002.jpg')
# img3 = cv2.imread('CV Rahmat Fabhian A_page-0003.jpg')

# txt = pytesseract.image_to_string(img) + pytesseract.image_to_string(img2) + pytesseract.image_to_string(img3)

# file = open('tes1.txt', 'w')
# file.write(txt)
# file.close()

# #programnya

# #variabel awal
# nilai = 100

print("Berikut merupakan hasil review kami: ")

#kriteria ada summary apa kaga
# def check():
#     with open('tes1.txt') as f:
#         datafile = f.readlines()
#     found = False 
#     for line in datafile:
#         if 'summary' in line:
#             return True
#     return False 

# if check():
#     nilai == nilai
# else:
#     nilai -= 10
#     print("Sertakan summary dari CV ini ya.")

# #kriteria ada linkedin apa kaga
# def check():
#     with open('tes1.txt') as f:
#         datafile = f.readlines()
#     found = False 
#     for line in datafile:
#         if 'linkedin' in line:
#             return True
#     return False 

# if check():
#     nilai == nilai
# else:
#     nilai -= 5
#     print("Sertakan laman linkedin kamu ya.")


# #print nilai akhirnya
# print("")
# print("Nilai CV anda adalah " + str(nilai) + "%")