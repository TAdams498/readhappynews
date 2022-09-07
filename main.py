#   Author: Thomas Adams
#   Description:    script to run all functionality to scrape reddit, process audio, create video, and upload
#   Created On: 08/12/2022

#imports
import scrape
import audio_creation
import video_creation
import upload
import Project
import os

if __name__ == "__main__":
    Project_File = Project.Project()
    #grab reddit content
    scrape.create_posts_csv(Project_File)
    #create voice line audio
    audio_creation.make_voice_lines(Project_File)
    #create video
    video_creation.make_video(Project_File)
    #upload video
    upload.upload_with_API(Project_File)
