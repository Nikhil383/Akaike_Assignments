import os
import requests

NEWSAPI_KEY =os.getenv("NEWSAPI_KEY")  #Fetching from environment variables

def fetch_news(company):
    """Fetches news articles from user input using NewsAPI."""
    url = f"https://newsapi.org/v2/everything?q={company}&apiKey={NEWSAPI_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch news.")
        return []

    data = response.json()
    articles = []

    for item in data.get("articles", [])[:10]:  # Limit to 10 articles
        articles.append({
            "Title": item["title"],
            "Summary": item.get("description", "No summary available")
        })

    return articles
