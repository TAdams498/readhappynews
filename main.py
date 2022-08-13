#   Author: Thomas Adams
#   Description:    script to run all functionality to scrape reddit, process audio, create video, and upload
#   Created On: 08/12/2022

#imports
import scrape
import audio_creation
import video_creation

if __name__ == "__main__":
    #grab reddit content
    scrape.create_posts_csv()
    #create voice line audio
    audio_creation.make_voice_lines()
    #create video
    video_creation.make_video()
    #upload video
