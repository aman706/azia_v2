import json
import os
from datetime import datetime

MEMORY_FILE = "memory/memory.json"
DATASET_FILE = "journal/empathy_dataset.txt"

# Ensure files exist
os.makedirs("memory", exist_ok=True)
os.makedirs("journal", exist_ok=True)
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump([], f)
if not os.path.exists(DATASET_FILE):
    open(DATASET_FILE, "w").close()

def update_memory(user_input, emotion):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = {
            "timestamp": timestamp,
            "input": user_input,
            "emotion": emotion
        }

        # Append to JSON memory
        with open(MEMORY_FILE, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.append(log)
            f.seek(0)
            json.dump(data, f, indent=4)

        # Append to empathy training log
        with open(DATASET_FILE, "a", encoding="utf-8") as df:
            df.write(f"[{timestamp}] {emotion.upper()}: {user_input}\n")

    except Exception as e:
        print(f"[Memory Save Error] {e}")
