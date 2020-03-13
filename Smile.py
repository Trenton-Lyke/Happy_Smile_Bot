
import pygame, time

from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile
from gpiozero import LED


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
#led object
led = LED(18)

#turns on LED
led.on()
#says yay I am smiling
textToSpeech("Yay I am smiling",'en',False)
#waits 60 seconds
time.sleep(60)

