from src.agents.reddit_agent import RedditAgent

if __name__ == "__main__":
    agent = RedditAgent()
    data = agent.get_reddit_data("SpaceX")
    print(data)
