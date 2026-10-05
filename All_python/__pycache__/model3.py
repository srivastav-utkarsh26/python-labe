import pyttsx3

engine = pyttsx3.init()

# Optional: adjust rate (default ~200) and volume (0.0–1.0)
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

engine.say("Hello! akshat Bhosadiwallae")
engine.runAndWait()   