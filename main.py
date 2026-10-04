import speech_recognition as sr
import webbrowser
import requests
import xml.etree.ElementTree as ET
import musicLibrary
import yt_dlp
import subprocess
import pyjokes
from google import genai
from google.genai import types


recognizer = sr.Recognizer()
def speak(text):
    subprocess.run(["say", text])

def get_news():
    url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    response = requests.get(url, timeout=10)
    root = ET.fromstring(response.content)
    titles = []
    for item in root.iter("item"):
        title = item.find("title").text.rsplit(" - ", 1)[0]
        titles.append(title)
    return titles[:5]

def play_on_youtube(query):
    with yt_dlp.YoutubeDL({"quiet": True, "extract_flat": True}) as ydl:
        info = ydl.extract_info(f"ytsearch1:{query}", download=False)
    video_id = info["entries"][0]["id"]
    webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")

client = genai.Client(api_key="YOUR_API_KEY_HERE")


def ask_ai(prompt):
    models = ["gemini-2.5-flash-lite", "gemini-2.5-flash", "gemini-3.5-flash"]
    for model_name in models:
        try:
            cfg = dict(
                system_instruction="You are Jarvis, a voice assistant. Answer in 1-2 short spoken sentences. No lists, no markdown.",
                max_output_tokens=100,
            )
            if "2.5" in model_name:
                cfg["thinking_config"] = types.ThinkingConfig(thinking_budget=0)
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(**cfg),
            )
            return response.text
        except Exception as e:
            print(model_name, "failed:", repr(e))
    return "Sorry, I can't reach my brain right now."



def listen_once():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout=8, phrase_time_limit=10)
    return r.recognize_google(audio)

def quiz_mode():
    speak("Quiz mode. Which subject?")
    try:
        topic = listen_once()
    except Exception:
        speak("I didn't catch that")
        return
    asked = []
    for i in range(3):
        question = ask_ai(f"Ask me one short quiz question about {topic}. Do not repeat: {asked}. Only the question.")
        asked.append(question)
        print(question)
        speak(question)
        try:
            answer = listen_once()
        except Exception:
            speak("I didn't hear an answer")
            continue
        verdict = ask_ai(f"Question: {question}\nMy answer: {answer}\nSay if I'm correct and give the right answer in one short sentence.")
        print(verdict)
        speak(verdict)
    speak("Quiz finished")

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open stackoverflow" in c.lower():
        webbrowser.open("https://stackoverflow.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://mail.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://twitter.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open reddit" in c.lower():
        webbrowser.open("https://www.reddit.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "open netflix" in c.lower():
        webbrowser.open("https://www.netflix.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://www.amazon.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://www.spotify.com")
    elif "open stackexchange" in c.lower():
        webbrowser.open("https://stackexchange.com")
    elif "open quora" in c.lower():
        webbrowser.open("https://www.quora.com")
    elif "open wikipedia" in c.lower():
        webbrowser.open("https://www.wikipedia.org")
    elif "open twitch" in c.lower():
        webbrowser.open("https://www.twitch.tv")
    elif "open discord" in c.lower():
        webbrowser.open("https://discord.com")
    elif "open zoom" in c.lower():
        webbrowser.open("https://zoom.us")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "", 1).strip()
        for name, link in musicLibrary.music.items():
            if song and (name in song or song in name):
                speak(f"Playing {name}")
                play_on_youtube(link)
                break
        else:
            speak("Song not found")      
    elif "news" in c.lower():
        speak("Here are the latest news headlines:")
        for headline in get_news():
            print(headline)
            speak(headline) 
    elif "joke" in c.lower():
        joke = pyjokes.get_joke(category="neutral")
        print(joke)
        speak(joke)
    elif "quiz" in c.lower():
        quiz_mode()
    else:
        answer = ask_ai(c)
        print(answer)
        speak(answer)                




if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        r = sr.Recognizer()
        r.pause_threshold = 0.5

        print("Say something!")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
                word = r.recognize_google(audio)
                print("Heard:", word)
                
                
                if(word.lower() ==  "jarvis"):
                    speak("yes sir, how can I help you?")
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = r.listen(source, timeout=5, phrase_time_limit=8)
                        command = r.recognize_google(audio)

                        processCommand(command)



        except Exception as e:
            print("Error; {0}".format(e))            
