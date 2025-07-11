import queue
import sounddevice as sd
import vosk
import json
import os
from core.tts import speak_text

model_path = "models/vosk-model-small-en-us-0.15"
if not os.path.exists(model_path):
    raise FileNotFoundError("Vosk model not found in /models directory.")

q = queue.Queue()
model = vosk.Model(model_path)
samplerate = 16000

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen_wake_word():
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").lower()
                print(f"[Voice] Heard: {text}")
                if "azia" in text:
                    speak_text("Yes? I'm here.")
                    break

