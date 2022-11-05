import PIL
import numpy as np
import cv2
import matplotlib.pyplot as mp
import matplotlib.image as image
from PIL import Image
from pytesseract import pytesseract


path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
image_path = r"C:/Users/KIIT/Desktop/samp_img_8.png"
img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img)
print(text)