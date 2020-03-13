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

def reply(text,tweetId):
    api.update_status(text,tweetId)

def getMentions(last_seen_id):
    return api.mentions_timeline(last_seen_id)
def retrieveLastSeenId():
    f_read = open("last_seen_id.txt",'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def storeLastSeenId(last_seen_id):
    f_write = open("last_seen_id.txt",'w')
    f_write.write(str(last_seen_id))
    f_write.close()
def getTimeline():
    return api.user_timeline()

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
last_seen_id=retrieveLastSeenId()
mentions = getMentions(last_seen_id)
for mention in reversed(mentions):
    if '#complimentme' in mention.text.lower():
        print("found compliment me")
        print("responding back")
        r = json.loads(requests.get('https://complimentr.com/api').text)
        replyCompliment = r['compliment']
        reply("@"+mention.user.screen_name+" "+replyCompliment,mention.id)
        textToSpeech("Replying "+ r['compliment'] +" to "+mention.user.screen_name,'en',False)
    last_seen_id = mention.id
storeLastSeenId(last_seen_id)
