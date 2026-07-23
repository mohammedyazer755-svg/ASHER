# 🤖 Asher — Personal AI Assistant

> A personal AI assistant built from scratch using Python, designed to learn, remember, and interact with its user.

## 📌 About Asher

Asher is a personal AI assistant project developed using Python.

The project started as a simple rule-based chatbot and is gradually evolving into a more intelligent personal assistant with:

* 🧠 Personal memory
* 💬 Natural language interaction
* 🗂️ Conversation history
* 🔧 Modular architecture
* 🔍 Memory search
* 🎤 Voice interaction
* 🌐 API integration
* 🤖 Future AI / LLM integration

The long-term goal is to build an assistant that can understand conversations, remember important information, interact naturally, and perform useful tasks.

---

## ✨ Features

### 🗣️ Conversation

Asher can respond to basic conversational inputs such as:

* Hello / Hi / Hey
* How are you?
* Thanks
* Yes / No
* Help

### 🧠 Memory System

Asher can remember personal information provided by the user.

Examples:

```text
My favourite movie is GOAT
My hobby is coding
I study at Sri Sairam Engineering College
My favourite food is Biriyani
```

The information is stored in a local JSON memory system.

### 🔎 Memory Retrieval

Asher can retrieve stored information from memory.

Example:

```text
YOU: What is my favourite movie?

ASHER: Your favourite movie is GOAT
```

### 📜 Conversation History

Asher can save conversations and retrieve previous chat history.

Supported features include:

* Save conversations
* View conversation history
* Clear conversation history

### 🧩 Modular Architecture

The project is divided into multiple Python modules to keep the code organized and maintainable.

```text
main.py
brain.py
memory.py
history.py
commands.py
conversation.py
nlu.py
patterns.py
search.py
utils.py
config.py
```

Each module has a specific responsibility.

---

## 🏗️ Project Structure

```text
Asher v.01/
│
├── main.py              # Main entry point
├── brain.py             # Core assistant logic
├── commands.py          # Command handling
├── conversation.py      # General conversation handling
├── memory.py            # Memory management
├── history.py           # Conversation history
├── nlu.py               # Natural language processing
├── patterns.py          # Memory and conversation patterns
├── search.py            # Memory search functionality
├── utils.py             # Utility functions such as speech output
├── config.py            # Configuration and user information
│
├── memory.json          # Personal memory database (local)
├── history.json         # Conversation history (local)
├── .env                 # Environment variables (local)
├── .gitignore           # Files excluded from Git
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Technologies Used

* **Python**
* **JSON**
* **Requests**
* **python-dotenv**
* **Object-oriented and modular programming concepts**
* **Rule-based Natural Language Processing**

Future technologies planned:

* Large Language Models (LLMs)
* AI APIs
* Speech Recognition
* Text-to-Speech
* Tool Calling
* Internet Search
* Machine Learning

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project

```bash
cd Asher
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `pip` is not recognized on Windows, use:

```bash
python -m pip install -r requirements.txt
```

or:

```bash
py -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
NAME=YourName
AGE=18
```

Do not upload your `.env` file to GitHub.

### 5. Run Asher

```bash
python main.py
```

---

## 💬 Example

```text
=========================
        ASHER V0.1
=========================

Hello Yazer!
I am Asher
Version 0.1
Ready to assist you.

YOU: My favourite movie is GOAT

ASHER: Okay! I'll remember that.

YOU: What is my favourite movie?

ASHER: Your favourite movie is GOAT
```

---

## 🧠 Learning Journey

Asher is also a personal learning project created to improve practical Python and AI development skills.

The project has been developed gradually while learning:

1. Python fundamentals
2. Functions
3. Dictionaries
4. JSON
5. File handling
6. APIs
7. Environment variables
8. Modular programming
9. Memory systems
10. Conversation history
11. Natural Language Processing
12. Software architecture

The goal is to learn by building a real project instead of only studying theory.

---

## 🛣️ Roadmap

### ✅ Completed

* [x] Basic Python chatbot
* [x] User interaction
* [x] Config management
* [x] Environment variables
* [x] Personal memory system
* [x] JSON memory storage
* [x] Conversation history
* [x] Dynamic memory commands
* [x] Basic natural language patterns
* [x] Modular project structure
* [x] Memory search
* [x] Rule-based NLU

### 🔄 In Progress

* [ ] Improved natural language understanding
* [ ] Better memory retrieval
* [ ] Smarter memory categorization
* [ ] Fuzzy memory matching
* [ ] Improved conversation flow

### 🔮 Future Plans

* [ ] Integrate an LLM
* [ ] AI-powered conversations
* [ ] Long-term intelligent memory
* [ ] Voice input
* [ ] Natural voice output
* [ ] Internet search
* [ ] Weather and other APIs
* [ ] Tool calling
* [ ] Task automation
* [ ] Computer interaction
* [ ] Vision capabilities
* [ ] Personalized AI behavior

---

## 🎯 Vision

The ultimate goal of Asher is to become a truly personalized AI assistant that understands its user, remembers important information, learns from interactions, and helps with everyday tasks.

> **Asher is not just a chatbot. It's a journey toward building my own AI assistant from scratch.**

---

## 👨‍💻 Developer

**Yazer**

B.Tech — Artificial Intelligence & Data Science

Sri Sairam Engineering College

---

## ⭐ Project Status

🚧 **Asher v0.1 — Under Active Development**

This project is continuously evolving as new concepts and technologies are learned and implemented.
