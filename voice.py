#   Author: Thomas Adams
#   Description: simple functional code to generate tiktok voices as needed. based on https://github.com/oscie57/tiktok-voice
#   Created On: 08/12/2022

#imports
import requests
import base64
import json
import os

#   generate_voice
#   creates voice line with tiktok voices
#   Input:  text        text for voice to speak
#           filename    name of file to put voice line into
#           speaker     speaker code for which voice to use
#   Output: filename    sound file filename
#
def generate_voice(text, filename, speaker="en_au_001"):
    #post request to tiktok
    req = requests.post(f"https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker={speaker}&req_text={text}&speaker_map_type=0")
    #extract voice data
    voiceData = [req.json()["data"]["v_str"]][0]
    #decode voice data
    voiceLine = base64.b64decode(voiceData)
    #write to file
    os.chdir("voices")
    sound_file = open(filename, "wb")
    sound_file.write(voiceLine)
    sound_file.close()
    os.chdir("..")
    return filename
