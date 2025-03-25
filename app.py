import gradio as gr
from utils import process_articles

def analyze_news(company):
    structured_data = process_articles(company)
    return structured_data, structured_data["Audio"]  # JSON output + Hindi TTS

iface = gr.Interface(
    fn=analyze_news,
    inputs=gr.Textbox(label="Enter Company Name"),
    outputs=[
        gr.JSON(label="News Analysis"),
        gr.Audio(label="Hindi Audio Output", type="filepath"),  # Play audio
    ],
    title="News Sentiment & Analysis",
    description="Enter a company name to analyze recent news articles, sentiment distribution, topic overlap, and comparative analysis.",
)

if __name__ == "__main__":
    iface.launch(share=True)  # Launch the interface
