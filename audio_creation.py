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
import voice


#   make_content_voice
#   create content voice lines with headlines from reddit
#   Input:  Project_File
#           tiktok_voice        tiktok voice to use
#           headline_amount     the number of headlines to read
#   Output: files         filenames for content mp3s
#
def make_content_voice(Project_File, tiktok_voice, headline_amount=3):
    todays_date = str(date.today())
    headlines = []  #headlines for voice to read
    #open todays posts csv file
    with open(Project_File.get_headlines_csv(), newline='') as csvfile:
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

    Project_File.set_headlines(headlines)
    #handle voice processing
    #files for each headline read
    files = []
    file_num = 0
    for line in headlines:
        filename = voice.generate_voice(line, f"{file_num}_content_{todays_date}.mp3", tiktok_voice)
        files.append(filename)
        file_num += 1
    return files


#   make_voice_lines
#   create text to speech voice lines to place into video
#   Input:  Project_File
#   Output: none
#
def make_voice_lines(Project_File):
    #get voice lines from voiceLines.ini
    config = configparser.ConfigParser()
    config.read("config.ini")
    intro_text = config["Voice Lines"]["intro_text"]
    outro_text = config["Voice Lines"]["outro_text"]
    headline_amount = int(config["Voice Lines"]["headline_count"])
    tiktok_voice = config["Voice Lines"]["voice"]
    Project_File.set_intro_text(intro_text)
    Project_File.set_outro_text(outro_text)

    #create intro voice
    intro_tts = voice.generate_voice(intro_text, "intro.mp3", tiktok_voice)
    Project_File.set_intro_audio(intro_tts)

    #create outro voice
    outro_tts = voice.generate_voice(outro_text, "outro.mp3", tiktok_voice)
    Project_File.set_outro_audio(outro_tts)

    #create content voice
    content_tts = make_content_voice(Project_File, tiktok_voice, headline_amount)
    Project_File.set_content_audio_clips(content_tts)
