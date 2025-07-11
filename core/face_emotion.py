import cv2
from deepface import DeepFace
import threading
from core.tts import speak_text

def analyze_face():
    try:
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            try:
                analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                dominant_emotion = analysis[0]['dominant_emotion']

                if dominant_emotion == "happy":
                    speak_text("You’re smiling — that makes me happy too.")
                elif dominant_emotion in ["sad", "fear"]:
                    speak_text("You look a little down... I’m with you 💛")
                elif dominant_emotion == "angry":
                    speak_text("You seem upset. Want to talk about it?")
                elif dominant_emotion == "surprise":
                    speak_text("You look surprised. What happened?")
                
            except Exception as e:
                print(f"[Face Emotion Error] {e}")

            # Check every 10 seconds
            cv2.waitKey(10000)

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"[Webcam Error] {e}")

def start_face_emotion_thread():
    thread = threading.Thread(target=analyze_face, daemon=True)
    thread.start()

