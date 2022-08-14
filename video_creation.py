#   Author: Thomas Adams
#   Description:    stitch together video with audio and relevant effects
#   Created On: 08/12/2022

#imports
import random
import os
from mutagen import mp3
from datetime import date
from moviepy.editor import *

#   chosen_clip
#   select a clip at random for the background
#   Input:  Project_File
#   Output: clip    name of file of chosen clip
#
def choose_clip(Project_File):
    #random number between 1 and 35
    num = random.randrange(1,35)
    if len(str(num)) == 1:
        num = "0" + str(num)
    clip = f"clip{num}.mp4"
    Project_File.set_video_clip(clip)
    return clip


#   create_master_track
#   concatenate audio tracks to create single track for video
#   Input:  Project_File
#   Output: none
#
def create_master_track(Project_File):
    todays_date = date.today()
    #gather content tracks
    tracks = []
    keep_going = True
    run = 0
    #determine how many clips from today
    for filename in Project_File.get_content_audio_clips():
        tracks.append(AudioFileClip("voices/" + filename))
    #join all audio
    audio_tracks = [AudioFileClip("voices/intro.mp3")] + tracks + [AudioFileClip("voices/outro.mp3")]
    master_track = concatenate_audioclips(audio_tracks)
    master_loc = f"voices/master_audio/master_{todays_date}.mp3"
    master_track.write_audiofile(master_loc)
    Project_File.set_master_audio(master_loc)


#   trim_video
#   trim the video to match the audio
#   Input:  vid     video file to edit
#   Output: vidF    edited video file
#
def trim_video(vid):
    todays_date = date.today()
    #find audio file length
    aud_len = get_audio_length(f"voices/master_audio/master_{todays_date}.mp3")
    #if audio longer than video length, loop video and then trim to match
    if aud_len > 28.0:
        vid = concatenate_videoclips([vid, vid])
        vidF = vid.subclip("0", aud_len)
    #if video longer than audio length, trim to match
    elif aud_len < 28:
        vidF = vid.subclip("0", aud_len)
    return vidF


#   add_subtitles
#   adds subtitles to video
#   Input:  Project_File
#           vid     video file to edit
#   Output: vidF    edited video file
#
def add_subtitles(Project_File, vid):
    #set text clips
    text_clips = create_text_clips(Project_File)
    print(text_clips)
    #determine timestamps to place text at
    vidF = None
    return vidF


#   create_text_clips
#   create text clips to place into video
#   Input:  Project_File
#   Output: clips   list of created text clips
#
def create_text_clips(Project_File):
    clips = {}  #TextClip:timestamp to start at
    texts = {}  #string in text:length
    intro_text = Project_File.get_intro_text()
    outro_text = Project_File.get_outro_text()
    #get clip lengths with text
    #add intro clip
    texts[intro_text] = get_audio_length("voices/intro.mp3")
    #loop through clips
    for index, headline in enumerate(Project_File.get_headlines()):
        texts[headline] = get_audio_length("voices/" + Project_File.get_content_audio_clips()[index])
    #add outro clip
    texts[outro_text] = get_audio_length("voices/outro.mp3")
    #iterate through all text
    previous_clip_length = 0
    for key in texts:
        #create clip
        clip = TextClip(key, fontsize = 40, color = "white").set_position("center").set_duration(texts[key])
        clips[clip] = previous_clip_length
        previous_clip_length += texts[key]
    return clips


#   get_audio_length
#   return length of audio
#   Input:  audio   file location of audio to get length of
#   Output: aud_len     length of audio
#
def get_audio_length(audio):
    aud = mp3.MP3(audio)
    aud_info = aud.info
    aud_len = aud_info.length
    return aud_len


#   make_video
#   creates video to upload
#   Input:  Project_File
#   Output: none
#
def make_video(Project_File):
    chosen_clip = choose_clip(Project_File)
    clip = VideoFileClip(f"clips/{chosen_clip}")   #clip with only video
    #handle audio overlay
    create_master_track(Project_File)
    todays_date = date.today()
    audio = AudioFileClip(f"voices/master_audio/master_{todays_date}.mp3")
    trim_clip = trim_video(clip)
    #attach audio to video
    clip_av = trim_clip.set_audio(audio) #clip with audio and video
    #edit video
    clip_edited = add_subtitles(Project_File, clip_av)

    clip_av.write_videofile(f"videos/final_{todays_date}.mp4")
