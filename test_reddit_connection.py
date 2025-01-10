import praw
import os
from dotenv import load_dotenv

load_dotenv()

try:
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )
    subreddit = reddit.subreddit("all")
    print("Connection successful. Displaying top 5 posts:\n")
    for post in subreddit.hot(limit=5):
        print(f"Title: {post.title}")
        print(f"URL: {post.url}")
        print(f"Score: {post.score}")
        print()
except Exception as e:
    print(f"Error: {e}")
