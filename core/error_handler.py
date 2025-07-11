import datetime
from core.tts import speak_text

LOG_FILE = "memory/error_log.txt"

def handle_error(error, chatbox=None):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    detailed = f"{timestamp} - {type(error).__name__}: {str(error)}\n"
    
    # Log to console
    print(detailed)
    
    # Voice feedback
    speak_text("Oops, I hit a little glitch, but I’m still here with you.")

    # GUI feedback (if chatbox exists)
    if chatbox:
        chatbox.insert("end", f"Azia: I'm okay, just had a small error.\n")
        chatbox.insert("end", f"{detailed}\n")

    # Save to log file
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log:
            log.write(detailed)
    except Exception as log_error:
        print(f"[Logging Error] Failed to save log: {log_error}")
