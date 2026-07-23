import json
def load_history():
    with open("history.json", "r") as file:
        data = json.load(file)
    return data

def save_history(data):
    with open("history.json", "w") as file:
        json.dump(data, file, indent=4)

def add_chat(sender, message):
    data = load_history()
    data["chat"].append({
        "sender": sender,
        "message": message  
    })

    save_history(data)

def show_history():
    data = load_history()
    for chat in data["chat"]:
        print(f"{chat['sender']}: {chat['message']}")
        
def clear_history():
    data={
        "chat":[]
    }
    save_history(data)