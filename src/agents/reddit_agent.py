import praw
import os
from dotenv import load_dotenv

class RedditAgent:
    def __init__(self):
        load_dotenv()
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
        )

    def get_reddit_data(self, query, subreddit="all", limit=5):
        """
        Fetch posts related to the query from the specified subreddit.
        """
        try:
            results = []
            for post in self.reddit.subreddit(subreddit).search(query, limit=limit):
                results.append({
                    "title": post.title,
                    "url": post.url,
                    "score": post.score,
                    "comments": post.num_comments,
                })
            return results
        except Exception as e:
            return {"error": f"Failed to fetch data from Reddit: {e}"}
