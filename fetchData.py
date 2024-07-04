import praw
import pandas as pd
from datetime import datetime, timezone

reddit = praw.Reddit(
    client_id='zv48-ZAaTgWdcRCv1KMiDw',
    client_secret='Cbln7P78Q7N65cjv4rcfqdeueDmtcA',
    user_agent='CMPT353_project'
)

# Define functions to grab posts data
def fetch_posts(subreddit, category, limit=1000):
    posts_data = []
    if category == 'top':
        posts = subreddit.top('year', limit=limit)
    elif category == 'controversial':
        posts = subreddit.controversial('year', limit=limit)

    for post in posts:
        post_time = datetime.fromtimestamp(post.created_utc, tz=timezone.utc)
        posts_data.append([
            post.title,
            post.selftext,
            post.score,
            post.id,
            post.subreddit.display_name,
            post.url,
            post.num_comments,
            post_time.strftime('%Y-%m-%d %H:%M:%S'),  # UTC time
            post.author.name if post.author else 'N/A',
            post.is_self,
            post.over_18,
            post.spoiler,
            post.upvote_ratio,
            post.ups,
            post.downs,
            post_time.strftime('%A'),  # Day of the week
            post_time.strftime('%H'),  # Hour of the day
        ])
    return posts_data

# Grab the first 1000 top posts
subreddit = reddit.subreddit('all')
top_posts_data = fetch_posts(subreddit, 'top', limit=1000)

# Convert to a DataFrame and save to CSV
top_df = pd.DataFrame(top_posts_data, columns=[
    'title', 'selftext', 'score', 'id', 'subreddit', 'url', 'num_comments',
    'created_local', 'author', 'is_self', 'over_18', 'spoiler', 'upvote_ratio', 'upvotes', 'downvotes', 'day_of_week', 'hour_of_day'
])
top_df.to_csv('reddit_top_posts.csv', index=False)
print("saved reddit_top_posts.csv")

# Grab the first 1000 controversial posts
controversial_posts_data = fetch_posts(subreddit, 'controversial', limit=1000)

# Convert to a DataFrame and save to CSV
controversial_df = pd.DataFrame(controversial_posts_data, columns=[
    'title', 'selftext', 'score', 'id', 'subreddit', 'url', 'num_comments',
    'created_local', 'author', 'is_self', 'over_18', 'spoiler', 'upvote_ratio', 'upvotes', 'downvotes', 'day_of_week', 'hour_of_day'
])
controversial_df.to_csv('reddit_controversial_posts.csv', index=False)
print("saved reddit_controversial_posts.csv")

