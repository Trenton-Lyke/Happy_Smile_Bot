
#imports for facial recognition
import numpy as np
import cv2
#import for limiting time
import time
#import for controlling LED
from gpiozero import LED

#cascade classifiers for detecting faces and smiles
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_smile.xml
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml') 

#first camera detected by computer
cap = cv2.VideoCapture(0)

#led controlled by pin 18
led = LED(18)

#loops for 60 seconds
oldTime=time.time()
while time.time() - oldTime < 60:
    #get iages from camera and converts it to grey scale
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detects faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    smiles=[]
    for (x, y, w, h) in faces:
        #creates rectangle around face in image
        cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = img[y:y + h, x:x + w]
        #detects smiles
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20) 

        for (sx, sy, sw, sh) in smiles:
            #creates rectangle around face in image
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
    #displays image 
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    #turns LEDs on if a face is detected
    if len(faces) != 0 and len(smiles) != 0:
        led.on()  
    else:
        led.off()
