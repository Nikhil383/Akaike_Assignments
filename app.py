import gradio as gr
from utils import process_articles

def analyze_news(company):
    """Fetch and analyze news about a company."""
    structured_data = process_articles(company)
    return structured_data, structured_data["Audio"]  # To Return JSON + Audio File

# To Define Gradio Interface with JSON + Audio Output
interface = gr.Interface(
    fn=analyze_news,
    inputs=gr.Textbox(label="Enter Company Name"),
    outputs=[
        gr.JSON(label="News Sentiment Analysis Output"),
        gr.Audio(label="Hindi Audio Summary")
    ],
    title="News Sentiment Analysis",
    description="Analyze recent news articles for sentiment, topic extraction, and generate Hindi TTS output."
)

if __name__ == "__main__":
    interface.launch(share=True)
