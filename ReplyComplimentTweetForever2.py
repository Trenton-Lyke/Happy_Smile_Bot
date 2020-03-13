#imports for getting random compliments from https://complimentr.com/api
import json
import requests

#import for timing replies
import time

#imports for text to speech
import pygame
from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile

#imports for tweeting
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

#replys to tweets with a given text and tweet id
def reply(text,tweetId):
    api.update_status(text,tweetId,count=1)

#gets the mentions coming after a certain id
def getMentions(last_seen_id):
    return api.mentions_timeline(last_seen_id)

#retrieves the last seen id from the last_seen_id.txt
def retrieveLastSeenId():
    f_read = open("last_seen_id.txt",'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

#writes the last seen id in the last_seen_id.txt
def storeLastSeenId(last_seen_id):
    f_write = open("last_seen_id.txt",'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    


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

#infinite loop with 30 second sleeping periods between iterations so the API
#will not reject request for doing too many too quickly
while True:
    
    #gets newest mentions based on last_seen_id.txt
    last_seen_id=retrieveLastSeenId()
    mentions = getMentions(last_seen_id)
    #loops through all mentions in reverse from oldest to newest
    
    
    for mention in reversed(mentions):
        #finds if the mention contains #complimentme
        if '#complimentme' in mention.text.lower() and last_seen_id != mention.id:
            print(mention.text.lower())
            #gets random compliment and responds to mention
            r = json.loads(requests.get('https://complimentr.com/api').text)
            replyCompliment = r['compliment']
            print(replyCompliment)
            #reply("@"+mention.user.screen_name+" "+replyCompliment,mention.id)
            #says reply outloud
            #textToSpeech("Replying "+ r['compliment'] +" to "+mention.user.screen_name,'en',False)
        #gets the last_seen_id looking through all the mentions
        last_seen_id = mention.id
    #stores the last seen id
    storeLastSeenId(last_seen_id)
    #waits for 30 seconds before executing the next iteration
    time.sleep(30)

