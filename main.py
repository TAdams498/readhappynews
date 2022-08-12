#   Author: Thomas Adams
#   Description:    script to run all functionality to scrape reddit, process audio, create video, and upload
#   Created On: 08/12/2022

#imports
import scrape
import audioCreation

if __name__ == "__main__":
    scrape.create_posts_csv()
    audioCreation.make_voice_lines()
