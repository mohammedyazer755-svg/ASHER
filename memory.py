import json

def load_memory():

    with open("memory.json", "r") as file:
        data = json.load(file)
    
    return data

def save_memory(data):
    with open ("memory.json", "w") as file:
        json.dump(data, file , indent=4)

def get_memory(key):
    data = load_memory()
    for item in data["memory"]:
        if item["key"] == key:
            return item["value"]
    return None

def remember(key, value):
    data = load_memory()
    for item in data["memory"]:
        if item["key"] == key:
            item["value"] =value
            save_memory(data)
            return
    data["memory"].append({
        "key": key,
        "value": value
    })
    save_memory(data)
