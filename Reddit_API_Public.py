#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt

text1 = input('Enter Reddit Client ID:  ')
text2 = input('Enter Reddit Client Secret Key:  ')
text3 = input('Enter Reddit User Agent:  ') 
text4 = input('Enter Reddit Username:  ')
text5 = input('Enter Reddit User Password:  ')
reddit = praw.Reddit(client_id=text1, \
                     client_secret=text2, \
                     user_agent=text3, \
                     username=text4, \
                     password=text5)
text6 = input('Enter Subreddit Name:  ')
subreddit = reddit.subreddit(text6)
text7 = input('Enter Subreddit Topic Limit (Integers only):  ')
top_subreddit = subreddit.top(limit=text7)

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


def get_date(created):
    return dt.datetime.fromtimestamp(created)
text8 = input('Enter FilePath with Filename  CSV format only:  ')
_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)
topics_data.to_csv(text8, index=False, encoding = 'utf-8') 