from gtts import gTTS
from deep_translator import GoogleTranslator

def generate_tts(text, output_path="static/output.mp3"):
    """Translate text to Hindi and generate TTS audio."""
    try:
        translated_text = GoogleTranslator(source="auto", target="hi").translate(text)
        tts = gTTS(text=translated_text, lang="hi")
        tts.save(output_path)
        return output_path
    except Exception as e:
        print("Error generating TTS:", e)
        return None
