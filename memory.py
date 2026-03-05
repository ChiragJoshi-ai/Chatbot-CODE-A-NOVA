import json
import os

DATA_FILE = "users.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def update_user(username, message):
    data = load_data()

    if username not in data:
        data[username] = {
            "history": [],
            "interests": []
        }

    # Save chat history
    data[username]["history"].append(message)

    # Detect interests
    msg = message.lower()

    if "python" in msg and "python" not in data[username]["interests"]:
        data[username]["interests"].append("python")

    if "ai" in msg and "ai" not in data[username]["interests"]:
        data[username]["interests"].append("ai")

    if "machine learning" in msg and "machine learning" not in data[username]["interests"]:
        data[username]["interests"].append("machine learning")

    save_data(data)


def generate_reply(username, message):
    data = load_data()

    if username not in data:
        return "Hello! Tell me about your interests."

    interests = data[username]["interests"]
    msg = message.lower()

    if "recommend" in msg:

        if "python" in interests:
            return "Since you're learning Python, try building small projects or practicing on LeetCode."

        if "ai" in interests:
            return "Since you like AI, try learning Machine Learning with Python using scikit-learn."

        return "Tell me your interests and I can recommend something."

    return "Got it. Tell me more!"