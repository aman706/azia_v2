import pyautogui
import pygetwindow as gw
import subprocess
import os

def run_task(command):
    command = command.lower()

    try:
        if "open notepad" in command:
            subprocess.Popen("notepad.exe")
            return "Notepad opened for you."

        elif "type" in command:
            to_type = command.split("type", 1)[1].strip()
            pyautogui.write(to_type, interval=0.05)
            return f"Typed: {to_type}"

        elif "minimize" in command:
            window = gw.getActiveWindow()
            if window:
                window.minimize()
                return "Window minimized."
            return "No window to minimize."

        elif "close window" in command:
            window = gw.getActiveWindow()
            if window:
                window.close()
                return "Closed the active window."

        elif "shutdown" in command:
            os.system("shutdown /s /t 1")
            return "Shutting down the system..."

        elif "restart" in command:
            os.system("shutdown /r /t 1")
            return "Restarting now..."

        else:
            return None  # Let other modules handle the rest

    except Exception as e:
        return f"Oops, task failed: {e}"
