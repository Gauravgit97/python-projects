import pytesseract   #to use this module you need to install tesseract application from its git-hub reposetory
import os
from PIL import Image



pytesseract.pytesseract.tesseract_cmd-r'full_path_where_teserect_installed'
def convert():
    img = Image.open('path.jpj')
    text = pytesseract.image_to_string(img)
    print(text)


convert()