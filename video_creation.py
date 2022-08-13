#   Author: Thomas Adams
#   Description:    stitch together video with audio and relevant effects
#   Created On: 08/12/2022

#imports
import random
from datetime import date
from moviepy.editor import *

#   chosen_clip
#   select a clip at random for the background
#   Input:  none
#   Output: clip    name of file of chosen clip
#
def choose_clip():
    #random number between 1 and 35
    num = random.randrange(1,35)
    if len(str(num)) == 1:
        num = "0" + str(num)
    clip = f"clip{num}.mp4"
    return clip


#   create_master_track
#   concatenate audio tracks to create single track for video
#   Input:  none
#   Output: none
#
def create_master_track():
    todays_date = date.today()
    audio_tracks = [AudioFileClip("voices/intro.mp3"), AudioFileClip(f"voices/content_{todays_date}.mp3"), AudioFileClip("voices/outro.mp3")]
    master_track = concatenate_audioclips(audio_tracks)
    master_track.write_audiofile(f"voices/master_audio/master_{todays_date}.mp3")


#   make_video
#   creates video to upload
#   Input:  none
#   Output: none
#
def make_video():
    chosen_clip = choose_clip()
    clip = VideoFileClip(f"clips/{chosen_clip}")   #clip with only video
    #handle audio overlay
    create_master_track()
    todays_date = date.today()
    audio = AudioFileClip(f"voices/master_audio/master_{todays_date}.mp3")
    #attach audio to video
    clip_av = clip.set_audio(audio) #clip with audio and video
    clip_av.write_videofile(f"videos/final_{todays_date}.mp4")
