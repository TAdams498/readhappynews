#   Author: Thomas Adams
#   Description: Scraper to retrieve /r/upliftingnews headlines from past 24 hours
#   Created on: 08/12/2022

#imports
import praw     #to handle python scraping
import pandas as pd
from datetime import date

#   create_posts_csv
#   create csv file containing information from todays top posts
#   Input:  none
#   Output: none
#
def create_posts_csv():
    #read-only praw instance
    reddit_read_only = praw.Reddit(client_id="LGDn1hg5MkEVWly3KXhEhA", client_secret="pg88IYqS2MU1jV8FqVTU8DSkPeXZRQ", user_agent="read-happy-news")
    subreddit = reddit_read_only.subreddit("upliftingnews")

    #grab posts
    posts = {"title": [], "id": [], "score": [], "img": []}
    for post in subreddit.top(time_filter="day"):
        #reject repeated headlines
        if post.title not in posts["title"]:
            posts["title"].append(post.title)
            posts["id"].append(post.id)
            posts["score"].append(post.score)
            posts["img"].append(get_thumbnail(post))

    #convert to panda dataframe
    panda_posts = pd.DataFrame(posts)
    #export to csv
    todays_date = str(date.today())
    panda_posts.to_csv("posts/posts-" + todays_date + ".csv", index=True)


#   get_thumbnail
#   retrieve post thumbnail to put in video
#   Input:  post   raw post data from subreddit
#   Output: location    local location of thumbnail
#
def get_thumbnail(post):
    if hasattr(post, "preview") == True:
        if "images" in post.preview:
            print("Submission has an image preview")
            preview_image_link = post.preview["images"][0]["source"]["url"]
            print(preview_image_link)
        else:
            print("Submission doesn't have an image preview")
            preview_image_link = ""
    else:
        print("Submission doesn't have a preview")
        preview_image_link = ""
    return 0
