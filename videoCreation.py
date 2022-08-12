#   Author: Thomas Adams
#   Description: handle video creation from results of scrape.py
#   Created on: 08/12/2022

from moviepy.editor import *
from gtts import gTTS
from playsound import playsound
import configparser
import csv
from datetime import date
import importlib
voice = importlib.import_module("tiktok-voice.main")

#   make_voice_lines
#   create text to speech voice lines to place into video
#   Input:  none
#   Output: none
#
def make_voice_lines():
    #get voice lines from voiceLines.ini
    config = configparser.ConfigParser()
    config.read("config.ini")
    intro_text = config["Voice Lines"]["intro_text"]
    outro_text = config["Voice Lines"]["outro_text"]
    headline_amount = int(config["Voice Lines"]["headline_count"])

    #create intro voice
    intro_tts = gTTS(intro_text, lang="en", tld="com.au")
    intro_tts.save("intro.mp3")

    #create outro voice
    outro_tts = gTTS(outro_text, lang="en", tld="com.au")
    outro_tts.save("outro.mp3")

    #create content voice
    content_tts = make_content_voice(headline_amount)
    content_tts.save("content.mp3")


#   make_content_voice
#   create content voice lines with headlines from reddit
#   Input:  headline_amount   the number of headlines to read
#   Output: tts         text to speech object for content voice lines
#
def make_content_voice(headline_amount=3):
    todays_date = str(date.today())
    headlines = []  #headlines for voice to read
    #open todays posts csv file
    with open("posts/posts-" + todays_date + ".csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        #read through number of headlines from posts
        iterations = 0
        for row in reader:
            #ignore first row
            if iterations > 0:
                headlines.append(row[1])
            #stop when desired number of headlines reached
            if iterations == headline_amount:
                break
            iterations += 1

    #handle voice processing
    content_text = ". ".join(headlines)
    tts = gTTS(content_text, lang="en", tld="com.au")
    return tts


def make_video():
    #premade video clip for background
    myclip = VideoFileClip("")

voice.main("hello","en_au_001")
