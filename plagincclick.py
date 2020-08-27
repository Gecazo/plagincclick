import cv2 as cv
import numpy as np
from PIL import ImageGrab
import pyautogui
import glob

average = [0, ]
templates = []
templ_shapes = []
threshold = 0.7

files = glob.glob(r"/tmp*.png") #path  

for myfile in files:
    image = cv.imread(myfile, 0)
    templates.append(image)

for _ in range(1000):
    base_screen = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    base_screen.save("\\base_screen.png") #path 

    img_rgb = cv.imread(r"/base_screen.png") #path 
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    for template in templates:
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            pyautogui.moveTo(pt[0] + w, pt[1] + h)
            print("aiming...")
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            break