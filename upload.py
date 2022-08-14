#   Author: Thomas Adams
#   Description:    handles all functionality for uploading videos to appropriate platforms
#   Created On: 08/13/2022

#imports
import os
import configparser
import Project
import random
from datetime import date

#   upload
#   upload videos to platforms
#   Input:  Project_File
#   Output: none
#
def upload(Project_File):
    todays_date = date.today()
    file = Project_File.get_final_video()
    category = "24"
    privacy_status = "public"
    title = choose_title()
    description = choose_description()
    config = configparser.ConfigParser()
    config.read("config.ini")
    keywords = config["Video"]["keywords"]
    #upload command
    os.system(f"python3 upload_video.py --file {file} --title {title} --description {description} --keywords {keywords} --category {category} --privacyStatus {privacy_status}")


#   choose_title
#   select a title from the list to put on the video
#   Input:  none
#   Output: title   the chosen title
#
def choose_title():
    config = configparser.ConfigParser()
    config.read("config.ini")
    possible_titles = config["Video"]["titles"]
    titles = possible_titles.split(", ")
    selection = random.randint(0,len(titles))
    title = titles[selection].capitalize()
    return title

#   choose_description
#   select a description from the list to put on the video
#   Input:  none
#   Output: description   the chosen description
#
def choose_description():
    config = configparser.ConfigParser()
    config.read("config.ini")
    possible_descriptions = config["Video"]["descriptions"]
    descriptions = possible_descriptions.split(", ")
    selection = random.randint(0,len(descriptions))
    description = descriptions[selection].capitalize()
    return description
