# News Summarization and Text-to-Speech Application

## Objective

Develop a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The tool should allow users to input a company name and receive a structured sentiment report along with an audio output.

## Folder Structure

## Workflow



## Models Used

Component: Model/Library Used
News Fetching: NewsAPI
Sentiment Analysis: TextBlob
Topic Extraction: YAKE
Article Comparison: SBERT (Sentence Transformers)
Text-to-Speech (Hindi): gTTS (Google Text-to-Speech)

## API Used

NewsAPI: To fetch latest news aritcles related to a given company

## Features

✅ Fetch & Summarize News Articles
✅ Perform Sentiment Analysis (Positive, Negative, Neutral)
✅ Extract Key Topics from News
✅ Compare Articles & Identify Differences
✅ Identify Common & Unique Topics across Articles
✅ Generate Hindi TTS Audio Output
✅ User-Friendly Gradio Interface for Interaction

## Assumptions and Limitations

### Assumptions

NewsAPI returns at least 10 articles per query (Fewer articles may affect topic extraction).
YAKE extracts meaningful topics from summaries (Short summaries may limit topic diversity).
Sentiment Analysis is based on TextBlob, which may not always be 100% accurate.

### Limitations

❌ Relies on NewsAPI, which has a request limit per day (Free Tier: 100 requests/day).

❌ Sentiment Analysis does not consider sarcasm or complex linguistic context.

❌ Hindi TTS uses Google’s gTTS, which may have minor pronunciation issues.

## Possible Improveents

🔹 Improve Sentiment Accuracy (Use fine-tuned transformer models like BERT).
🔹 Enhance Topic Extraction (Combine YAKE with LDA for better results).
🔹 Support Multiple Languages (Allow users to choose output language for TTS).
🔹 Include More Data Sources (Extend beyond NewsAPI using web scraping).
🔹 Deploy on Hugging Face Spaces & GitHub Actions for Continuous Deployment.

## Setup & Installation

1. Clone the Repository

git clone https://github.com/yourusername/news_summary_project.git
cd news_summary_project

2. Install the Dependancies

pip install -r requirements.txt

3. Setup Environment Variables

NEWS_API_KEY=your_newsapi_key

4. Run the Application

python app.py

## Deployment

it has been deployed on hugging face spaces(link provided below): https://huggingface.co/spaces/Nikhillmahesh701/Akaike_Assignments

## Screenshot
![image](https://github.com/user-attachments/assets/15406c5f-3fd3-416a-9bbe-5f0fcf4ee7d7)

![image](https://github.com/user-attachments/assets/d5bc2a9b-736f-47db-a9e6-7d8abc8c7e7e)

## Credits

developed by Nikhil Mahesh | Github: Nikhil383
contact: nikhilmahesh89@Gmail.com
