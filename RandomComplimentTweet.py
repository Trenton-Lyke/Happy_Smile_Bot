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

CONSUMER_KEY='d0aIhxfvI2IWQHQNpknNXWAag'
CONSUMER_SECRET='i5Cck7M7QQvCLcvacw2aqGc199UEnvg4DiXAX0N9ybbtBH3UQ4'
ACCESS_KEY='1234707563259756544-8hadNsiZK5omAJCOxO2GMp0yd6S9em'
ACCESS_SECRET='KFeNLA1cwkUpb5xITZnG6p4aFOMBcddjvN86XkT2jtGtS'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet(text):
    api.update_status(text)

def textToSpeech(text,language,isSlow):

  

  
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    textToSpeechEngine = gTTS(text=text, lang=language, slow=isSlow) 
      
    # Saving the converted audio in a mp3 file named 
    # welcome  
    sf = TemporaryFile()
    textToSpeechEngine.write_to_fp(sf)
    sf.seek(0)
    mixer.music.load(sf)

    ##os.system("start welcome.mp3")
    
    
    mixer.music.play()
    

    while not pygame.mixer.music.get_pos() == -1:
        pass

mixer.init()
r = json.loads(requests.get('https://complimentr.com/api').text)
textToSpeech("Tweeting "+r['compliment'],'en',False)
tweet(r['compliment'])
