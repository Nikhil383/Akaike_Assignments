import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load API keys from .env file
NEWS_API_KEY = "0920fb558a844ebeaf63bc1b51435653" #os.getenv("NEWS_API_KEY")

def fetch_news(company):
    """Fetch top 10 news articles related to the company using NewsAPI."""
    url = f"https://newsapi.org/v2/everything?q={company}&language=en&pageSize=10&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching news:", response.text)
        return []

    data = response.json()
    articles = []

    for item in data.get("articles", [])[:10]:
        articles.append({
            "Title": item.get("title", "No Title"),
            "Summary": item.get("description", "No summary available")
        })

    return articles
