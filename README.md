<h1 align="center">🧠 Chatbot with Memory</h1>

<p align="center">
A simple chatbot that remembers users and provides context-aware replies.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)
![Project](https://img.shields.io/badge/Project-Chatbot-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</p>

---

## 📌 About The Project

This project is a **Flask-based chatbot** that can remember user conversations and detect interests from messages.

Instead of responding blindly, the chatbot stores chat history and uses it to provide **context-aware recommendations**.

It demonstrates the basic idea of **memory in conversational systems** using simple JSON storage.

---

## ✨ Features

🧠 Stores user chat history  
🔎 Detects user interests automatically  
💬 Context-aware replies  
💾 Persistent memory using JSON  
🌐 Simple web interface with Flask  

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|--------|
| Python | Backend logic |
| Flask | Web framework |
| HTML / CSS | Frontend |
| JSON | Memory storage |

---

## 📂 Project Structure

```
chatbot-memory-flask
│
├── app.py
├── memory.py
├── requirements.txt
│
└── templates
      └── index.html
```

---

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/ChiragJoshi-ai/Chatbot-CODE-A-NOVA/
```

Install dependencies

```
uv pip install flask
```

Run the project

```
python app.py
```


---

## ⚡ Quick Demo

User message:

```
I am learning python
```

Bot stores interest → **python**

User message:

```
recommend something
```

Bot reply:

```
Since you're learning Python, try building small projects or practicing on LeetCode.
```

---

## 🧠 Example Memory Storage

```
{
  "chirag": {
    "history": [
      "I am learning python",
      "recommend something"
    ],
    "interests": [
      "python"
    ]
  }
}
```

The chatbot stores this information in **users.json**, allowing it to remember previous conversations.

---

## 🎯 Future Improvements

🚀 AI-powered responses  
📊 Better chat UI  
🧠 Vector-based memory storage  
🤖 LLM integration  

---

## 👨‍💻 Author

**Chirag Joshi**  
B.Tech Computer Science & Engineering  

GitHub:  
https://github.com/ChiragJoshi-ai
