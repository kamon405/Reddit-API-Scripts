#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import getpass

text1 = input('Enter Reddit Client ID:  ')
text2 = getpass.getpass('Enter Reddit Client Secret Key:  ')
text3 = input('Enter Reddit User Agent:  ') 
text4 = input('Enter Reddit Username:  ')
text5 = getpass.getpass('Enter Reddit User Password:  ')
reddit = praw.Reddit(client_id=text1, \
                     client_secret=text2, \
                     user_agent=text3, \
                     username=text4, \
                     password=text5)
text6 = input('Enter Subreddit Name:  ')
subreddit = reddit.subreddit(text6)

top_subreddit = subreddit.top(limit=200000) #edit the post limit in script as int

topics_dict = { "title":[], \
                "score":[], \
                "id":[], \
                "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

import datetime
basename = "File"
suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S%f")
extension = ".csv"
filename = "_".join([basename, suffix, extension]) # e.g. 'file_120508_171442'

def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)
topics_data.to_csv(filename, index=False, encoding = 'utf-8') 
print('Data Pull Complete!!')