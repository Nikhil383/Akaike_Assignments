import requests
import yake
from textblob import TextBlob
from sentence_transformers import SentenceTransformer, util
from services.news_fetcher import fetch_news
from tts import generate_tts

# Initialize SBERT & YAKE
sbert_model = SentenceTransformer("all-MiniLM-L6-v2")
yake_extractor = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, top=5)

def analyze_sentiment(text):
    """Perform sentiment analysis using TextBlob."""
    if not text or not isinstance(text, str) or not text.strip():
        return "Neutral"
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

def extract_topics(text):
    """Extract key topics using YAKE and return as a list."""
    if not text or not isinstance(text, str) or not text.strip():
        return []

    keywords = yake_extractor.extract_keywords(text)
    return [kw[0] for kw in keywords]  # Ensure it's a proper list

def extract_common_and_unique_topics(articles):
    """Identify common topics appearing in multiple articles and extract unique topics."""
    topic_sets = {}

    for i, article in enumerate(articles):
        topics = extract_topics(article["Summary"])
        topic_sets[f"Article {i+1}"] = set(topics)

    all_topics = [topic for topics in topic_sets.values() for topic in topics]
    common_topics = list({topic for topic in all_topics if all_topics.count(topic) > 1})  # Convert to list

    unique_topics = {
        f"Unique Topics in Article {i+1}": list(topics - set(common_topics)) for i, topics in enumerate(topic_sets.values())
    }

    return {"Common Topics": common_topics, **unique_topics}  # Proper list format

def compare_articles(articles):
    """Generate coverage differences by comparing specific article pairs."""
    comparisons = []
    pairs = [(0,1), (2,3), (4,5), (6,7), (8,9)]

    summaries = [article["Summary"] for article in articles]
    embeddings = sbert_model.encode(summaries, convert_to_tensor=True)

    for i, j in pairs:
        if i < len(articles) and j < len(articles):
            comparison_text = f"Article {i+1} discusses '{articles[i]['Title']}', while Article {j+1} focuses on '{articles[j]['Title']}'."
            impact_text = (
                f"The first article has a {articles[i]['Sentiment']} sentiment, whereas the second has a {articles[j]['Sentiment']} sentiment. "
                f"This contrast may influence public perception differently."
            )
            comparisons.append({"Comparison": comparison_text, "Impact": impact_text})

    return comparisons  # Ensure list format

def process_articles(company):
    """Processes articles to extract sentiment, topics, and comparisons."""
    articles = fetch_news(company)
    structured_data = {"Company": company, "Articles": []}
    sentiments = []

    for article in articles:
        summary = article.get("Summary", "No summary available")
        sentiment = analyze_sentiment(summary)
        topics = extract_topics(summary)  # Properly formatted list
        sentiments.append(sentiment)

        structured_data["Articles"].append({
            "Title": article["Title"],
            "Summary": summary,
            "Sentiment": sentiment,
            "Topics": topics  #Ensure Topics appear as list
        })

    # To Ensure Sentiment Distribution Exists
    sentiment_distribution = {s: sentiments.count(s) for s in ["Positive", "Negative", "Neutral"]}
    
    # To Ensure Comparative Sentiment Score is Assigned
    structured_data["Comparative Sentiment Score"] = {
        "Sentiment Distribution": sentiment_distribution,
        "Coverage Differences": compare_articles(structured_data["Articles"]),  # Proper list format
        "Topic Overlap": extract_common_and_unique_topics(structured_data["Articles"])  # Proper list format
    }

    # Ensure Final Sentiment Analysis is Present
    max_sentiment = max(sentiment_distribution, key=sentiment_distribution.get)
    final_sentiment_text = f"{company} latest news coverage is mostly {max_sentiment}."
    structured_data["Final Sentiment Analysis"] = final_sentiment_text

    # Ensure Hindi Audio is Generated
    structured_data["Audio"] = generate_tts(final_sentiment_text)

    return structured_data
