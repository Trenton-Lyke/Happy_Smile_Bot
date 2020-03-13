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

def didAlreadyTweetToday():
    timeline = getTimeline()
    for aTweet in timeline:
        if aTweet.created_at.date() == datetime.datetime.today().date():
            return True
    return False
def isConnectedToInternet():
    try:
        url="https://www.google.com"
        urllib.urlopen(url)
        return True
    except:
        return False
def textToSpeech(text,language,isSlow,isSolid):

  

  
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
        if isSolid:
            led.on()
        else:
            led.on()
            time.sleep(.05)
            led.off()
            time.sleep(.05)
            led.on()
            time.sleep(.05)
            led.off()
            time.sleep(.05)
  
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml') 


cap = cv2.VideoCapture(0)


complimentFileName="compliments.txt"
smiledBefore=False
led = LED(18)
mixer.init()
lastCompliment = ""
compliments = []
alreadySubmitted = False
lastDay=datetime.datetime.today().date()
tweetedToday=True
hadIssue=False
isConnected=True
try:
    tweetedToday=didAlreadyTweetToday()
except:
    isConnected=False
    hadIssue=True
with open(complimentFileName, "r") as file:
    for line in file:
        if line != "":
            compliments.append(line.replace("\n",""))
print(compliments)
oldTime=time.time()
while True:
    #if not isConnected:
    #    if isConnectedToInternet():
    #        tweetedToday=didAlreadyTweetToday()
    #        isConnected = True
    if lastDay != datetime.datetime.today().date():
        tweetedToday=False
        lastDay = datetime.datetime.today().date()
    try:
        timestamp = datetime.datetime.now().time()
        
        if not tweetedToday and len(compliments)>0 and timestamp >= datetime.time(8,0) and timestamp <= datetime.time(9,30):
            
            compliment=compliments[random.randint(0,len(compliments)-1)]
            tweet(compliment)
            compliments=[]
            lastCompliment=""
            tweetedToday=True
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
        if len(faces) != 0 and len(smiles) == 0:
            r = json.loads(requests.get('https://complimentr.com/api').text)
            lastCompliment = r['compliment']
            print(compliments)
            textToSpeech(r['compliment'],'en',False,False)
        elif len(faces) != 0 and len(smiles) != 0:
            if not smiledBefore:
                textToSpeech("Yaaaay you smiled!",'en',False,True)
                if lastCompliment != "":
                    compliments.append(lastCompliment)
                    lastCompliment=""
                    complimentsForFile=""
                    with open(complimentFileName, "w") as file:
                        for aCompliment in compliments:
                            complimentsForFile = complimentsForFile + aCompliment+"\n"
                        file.write(complimentsForFile)
                        
            smiledBefore=True
        else:
            led.off()
            smiledBefore=False
        if hadIssue:
            tweetedToday=didAlreadyTweetToday()
            hadIssue=False
        if time.time()-oldTime >=600:
            last_seen_id=retrieveLastSeenId()
            mentions = getMentions(last_seen_id)
            for mention in reversed(mentions):
                if '#complimentme' in mention.text.lower():
                    print("found compliment me")
                    print("responding back")
                    r = json.loads(requests.get('https://complimentr.com/api').text)
                    replyCompliment = r['compliment']
                    reply("@"+mention.user.screen_name+" "+replyCompliment,mention.id)
                    textToSpeech("Replying "+ r['compliment'] +" to "+mention.user.screen_name,'en',False,False)
                last_seen_id = mention.id
            storeLastSeenId(last_seen_id)
            oldTime=time.time()
    except Exception as e:
        print(e)
        #if not isConnectedToInternet():
        #    print("Raspberry Pi Offline...")
        #    isConnected = False
        #else:
        print("There was an issue with the program. Make sure you are connected to the internet and all the devices are plugged in.")
        hadIssue=True
    

cap.release()
cv2.destroyAllWindows()
