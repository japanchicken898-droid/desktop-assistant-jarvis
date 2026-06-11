# desktop-assistant-jarvis
# 🕶️ JARVIS - Voice-Activated Desktop Assistant

A Python-based desktop assistant inspired by Iron Man's JARVIS. This project leverages speech-to-text and text-to-speech technologies to listen to vocal commands, speak back to you, automate browser tasks, extract information from the web, and control local system applications.

## ✨ Features
- **Voice Recognition**: Converts your spoken commands into text in real-time using Google's Speech Recognition API.
- **Natural Text-To-Speech**: Speaks back to you with custom volume, speech rate, and gender-assigned voice profiles.
- **Dynamic Greetings**: Welcomes you automatically based on the time of day (Morning, Afternoon, Evening).
- **Automation Macros**: 
  - Searches Wikipedia summaries directly from your voice prompt.
  - Automatically launches major websites like Google and YouTube.
  - Checks current system time.
  - Opens local operating system utilities (like Notepad).

---

## 🛠️ Prerequisites & Installation

### 1. Install Required Python Packages
Open your terminal or command prompt and run the following command to install the necessary libraries:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyaudio
