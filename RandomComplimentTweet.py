#imports for getting compliments from https://complimentr.com/api
import json
import requests

#imports for text to speech
import pygame
from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile

#imports for twitter api
import tweepy

#api authentication variables
CONSUMER_KEY='d0aIhxfvI2IWQHQNpknNXWAag'
CONSUMER_SECRET='i5Cck7M7QQvCLcvacw2aqGc199UEnvg4DiXAX0N9ybbtBH3UQ4'
ACCESS_KEY='1234707563259756544-8hadNsiZK5omAJCOxO2GMp0yd6S9em'
ACCESS_SECRET='KFeNLA1cwkUpb5xITZnG6p4aFOMBcddjvN86XkT2jtGtS'

#authenticates to use twitter api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#tweets given text
def tweet(text):
    api.update_status(text)

#says input text outloud
def textToSpeech(text,language,isSlow):

  

  
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    textToSpeechEngine = gTTS(text=text, lang=language, slow=isSlow) 
      
    # Saving the converted audio in a mp3 temporary file  
    sf = TemporaryFile()
    textToSpeechEngine.write_to_fp(sf)
    sf.seek(0)

    #loads and plays temporary mp3
    mixer.music.load(sf)

    mixer.music.play()
    
    #waits till the mp3 is done playing
    while not pygame.mixer.music.get_pos() == -1:
        pass

#initializes mixer so it can play speeches
mixer.init()

#gets compliment from online api
r = json.loads(requests.get('https://complimentr.com/api').text)

#says what is going to be tweeted
textToSpeech("Tweeting "+r['compliment'],'en',False)

#tweets compliment
tweet(r['compliment'])
