#   Author: Thomas Adams
#   Description:
#   Created On: 08/13/2022

#imports
from datetime import date

class Project:
    def __init__(self, video_clip=None, intro_audio=None, outro_audio=None, content_audio_clips=[], master_audio=None, headlines=[], headlines_csv=None, todays_date=date.today(), intro_text="", outro_text="", final_video=None):
        self.video_clip = video_clip    #randomly chosen video clip
        self.intro_audio = intro_audio  #introduction audio clip
        self.outro_audio = outro_audio  #outro audio clip
        self.content_audio_clips = content_audio_clips  #audio clips speaking headlines
        self.master_audio = master_audio    #master audio clip
        self.headlines = headlines  #headlines
        self.headlines_csv = headlines_csv  #headlines csv
        self.todays_date = todays_date    #date object is created
        self.intro_text = intro_text    #intro text
        self.outro_text = outro_text    #outro text
        self.final_video = final_video  #final video product to be uploaded

    def get_video_clip(self):
    	return self.video_clip

    def set_video_clip(self, set):
    	self.video_clip = set

    def get_intro_audio(self):
    	return self.intro_audio

    def set_intro_audio(self, set):
    	self.intro_audio = set

    def get_outro_audio(self):
    	return self.outro_audio

    def set_outro_audio(self, set):
    	self.outro_audio = set

    def get_content_audio_clips(self):
    	return self.content_audio_clips

    def set_content_audio_clips(self, set):
    	self.content_audio_clips = set

    def get_master_audio(self):
    	return self.master_audio

    def set_master_audio(self, set):
    	self.master_audio = set

    def get_headlines(self):
    	return self.headlines

    def set_headlines(self, set):
    	self.headlines = set

    def get_headlines_csv(self):
    	return self.headlines_csv

    def set_headlines_csv(self, set):
    	self.headlines_csv = set

    def get_todays_date(self):
    	return self.todays_date

    def set_todays_date(self, set):
    	self.todays_date = set

    def get_intro_text(self):
    	return self.intro_text

    def set_intro_text(self, set):
    	self.intro_text = set

    def get_outro_text(self):
    	return self.outro_text

    def set_outro_text(self, set):
    	self.outro_text = set

    def get_final_video(self):
    	return self.final_video

    def set_final_video(self, set):
    	self.final_video = set

    def return_all(self):
        attributes = [self.video_clip, self.intro_audio, self.outro_audio, self.content_audio_clips, self.master_audio, self.headlines, self.headlines_csv, self.todays_date]
        return attributes
