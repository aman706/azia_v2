from main_gui import launch_gui
from core.voice_wake import listen_wake_word

if __name__ == "__main__":
    print("🔊 Waiting for wake word: 'Azia'...")
    listen_wake_word()
    launch_gui()
