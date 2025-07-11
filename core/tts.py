import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Try to set a calm female voice
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 155)  # Calmer speech speed

def speak_text(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"[TTS Error] {e}")
