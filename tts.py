from gtts import gTTS
from deep_translator import GoogleTranslator
import os

def generate_tts(text, lang="hi"):
    """Translate text to Hindi and generate TTS audio."""
    translator = GoogleTranslator(source="auto", target="hi")  # Translate to Hindi
    translated_text = translator.translate(text)

    output_path = "static/output.mp3"
    tts = gTTS(translated_text, lang=lang)
    tts.save(output_path)

    return output_path  # Return file path for playback
