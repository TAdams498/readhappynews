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
    #old URL post = f"https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker={speaker}&req_text={text}&speaker_map_type=0"
    post = f"https://api22-normal-c-useast1a.tiktokv.com/media/api/text/speech/invoke/?text_speaker={speaker}&req_text={text}&speaker_map_type=0&aid=1233"
    headers = {
        'User-Agent': 'com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)',
        'Cookie': 'sessionid=57b7d8b3e04228a24cc1e6d25387603a'
    }
    req = requests.post(post, headers=headers)
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
