# 🎙️ Jarvis: AI Voice Assistant

Jarvis is a voice-controlled desktop assistant built with Python. Say **"Jarvis"** to wake it up, then talk to it. It plays music, tells jokes, reads the news, opens websites, quizzes you, and answers questions using AI.

## ✨ Features

- 🎵 **Music player**: say "play "song name " and the song opens on YouTube
- 🤖 **AI powered**: ask anything and get a short spoken answer from Google Gemini(but use your own API key)
- 😂 **Jokes**: say "tell me a joke" for a random joke
- 📰 **News**: reads out the top headlines
- 🧠 **Quiz mode**: pick any subject and Jarvis asks you questions and checks your spoken answers
- 🌐 **Open websites**: opens popular sites like Google, YouTube, GitHub, Gmail, Instagram and more with a voice command

## 🗣️ Example commands

| You say | Jarvis does |
|---|---|
| "Jarvis" | Wakes up and listens |
| "Open YouTube" | Opens YouTube |
| "Play Mini Cooper" | Finds and plays the song |
| "News" | Reads the top headlines |
| "Tell me a joke" | Tells a joke |
| "Quiz me" | Starts a 3-question quiz |
| "What is a robot?" | Answers using AI |

## 🛠️ Tech stack

- Python 3
- SpeechRecognition (speech to text)
- macOS `say` command (text to speech)
- Google Gemini API (AI answers and quiz)
- yt-dlp (finds songs on YouTube)
- pyjokes, requests

## ⚙️ Setup

1. Clone the repo:
   ```
   git clone https://github.com/yashrana001/jarvis-voice-assistant.git
   cd jarvis-voice-assistant
   ```
2. Install the system tools (Mac):
   ```
   brew install portaudio flac
   ```
3. Install the Python packages:
   ```
   pip install SpeechRecognition pyaudio yt-dlp requests pyjokes google-genai
   ```
4. Get a free API key from [Google AI Studio](https://aistudio.google.com) and paste it in `main.py` where it says `YOUR_API_KEY_HERE`.
5. Run it:
   ```
   python main.py
   ```

## 📁 Project structure

```
├── main.py            # Main assistant logic
├── musicLibrary.py    # Song list
└── README.md
```

## 📝 Notes

- Built for **macOS** (uses the `say` command for speech).
- Needs an internet connection and microphone permission.
- To add songs, edit `musicLibrary.py`. To add websites, add another `elif` in `processCommand`.
- Never upload your real API key to GitHub.

## 🚀 Future improvements

- Weather updates
- Reminders and notes
- Controlling Mac apps and volume
- Windows and Linux support

## 👨‍💻 Author

Built by **Yash**
