import datetime
import json
import numpy as np
import cv2
import pygame, time
import requests
from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile
from gpiozero import LED
import tweepy
import random
import urllib

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml') 


cap = cv2.VideoCapture(0)

led = LED(18)
mixer.init()
oldTime=time.time()
while time.time() - oldTime < 60:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    smiles=[]
    for (x, y, w, h) in faces: 
        cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = img[y:y + h, x:x + w] 
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20) 

        for (sx, sy, sw, sh) in smiles: 
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if len(faces) != 0 and len(smiles) != 0:
        led.on()  
    else:
        led.off()
