import tkinter as tk
from tkinter import scrolledtext
from core.tts import speak_text
from core.emotion_ai import detect_emotion, generate_emotional_reply
from core.search import search_web
from core.tasks import run_task
from core.learn import update_memory
from core.face_emotion import start_face_emotion_thread

def handle_input(user_input, chatbox):
    chatbox.insert(tk.END, f"You: {user_input}\n")

    task_result = run_task(user_input)
    if task_result:
        chatbox.insert(tk.END, f"Azia: {task_result}\n")
        speak_text(task_result)
        return

    if "who" in user_input.lower() or "what" in user_input.lower():
        result = search_web(user_input)
        chatbox.insert(tk.END, f"Azia: {result}\n")
        speak_text(result)
        return

    mood = detect_emotion(user_input)
    reply = generate_emotional_reply(user_input, mood)
    update_memory(user_input, mood)
    chatbox.insert(tk.END, f"Azia: {reply}\n")
    speak_text(reply)

def launch_gui():
    start_face_emotion_thread()

    window = tk.Tk()
    window.title("Azia - Your AI Companion")
    window.geometry("600x700")
    window.configure(bg="#1f1f2e")

    title = tk.Label(window, text="Azia", font=("Helvetica", 24, "bold"), bg="#1f1f2e", fg="#e0e0ff")
    title.pack(pady=10)

    chatbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=25, font=("Consolas", 12), bg="#2a2a3d", fg="white")
    chatbox.pack(pady=10)
    chatbox.insert(tk.END, "Azia (Chat Mode) is ready. Type your query or 'exit' to quit.\n\n")

    entry = tk.Entry(window, font=("Consolas", 14), bg="#333344", fg="white", insertbackground="white", width=45)
    entry.pack(pady=5)

    def on_enter(event=None):
        user_input = entry.get()
        entry.delete(0, tk.END)
        if user_input.lower() == "exit":
            window.destroy()
        else:
            handle_input(user_input, chatbox)

    entry.bind("<Return>", on_enter)

    send_btn = tk.Button(window, text="Send", command=on_enter, bg="#5566dd", fg="white", font=("Helvetica", 12, "bold"))
    send_btn.pack(pady=10)

    window.mainloop()
