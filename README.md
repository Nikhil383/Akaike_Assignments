# News Summarization and Text-to-Speech Application

## Objective

To Develop a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The tool should allow users to input a company name and receive a structured sentiment report along with an audio output.

## Folder Structure

1. app.py-Main Gradio application that processes user input, fetches news, and displays results.
2. requirements.txt-Lists Python dependencies needed to run the project.
3. README.md-Documentation with project details, setup instructions, and API usage.
4. services/news_fetcher.py- Fetches news articles from NewsAPI.
5. utils.py- Handles sentiment analysis, topic extraction, and comparison of news articles.
6. tts.py- Converts sentiment analysis results into Hindi TTS audio.
7. static/output.mp3- Stores generated Hindi speech audio for playback.

## Workflow

1️⃣ User Input: The user enters a company name in the Gradio interface.

2️⃣ Fetch News: The system calls NewsAPI to fetch the latest 10 articles related to the company.

3️⃣ Summarization: Extracts a summary of each article if necessary.

4️⃣ Sentiment Analysis: Uses TextBlob to analyze the sentiment (Positive, Negative, or Neutral).

5️⃣ Topic Extraction: Uses YAKE (Keyword Extraction) to identify the main topics in each article.

6️⃣ Comparative Analysis:

Sentiment Distribution: Counts how many articles are Positive, Negative, and Neutral.

Coverage Differences: Compares pairs of articles (1-2, 3-4, etc.) for differences in reporting.

Topic Overlap: Identifies common topics and unique topics per article.
7️⃣ Final Sentiment Analysis: Determines overall sentiment based on article distribution.
8️⃣ Hindi TTS Generation: Converts the final sentiment text into Hindi speech for playback.
9️⃣ Display Results: The structured JSON output, topics, coverage differences, and audio are displayed in the Gradio UI.

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

The deploymenton has been done hugging face spaces(link provided below): https://huggingface.co/spaces/Nikhillmahesh701/Akaike_Assignments

## Screenshot
![image](https://github.com/user-attachments/assets/15406c5f-3fd3-416a-9bbe-5f0fcf4ee7d7)

![image](https://github.com/user-attachments/assets/d5bc2a9b-736f-47db-a9e6-7d8abc8c7e7e)

## Credits

developed by Nikhil Mahesh | Github: Nikhil383
contact: nikhilmahesh89@Gmail.com
