from history import add_chat

def speak(message):
    print(f"Asher: {message}")
    add_chat("Asher", message)