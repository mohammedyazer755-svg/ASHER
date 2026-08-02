import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "memory.json")


def load_memory():
    """
    Load memory.json and return its complete structure.
    """

    if not os.path.exists(MEMORY_FILE):
        return {"memory": []}

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            return {"memory": []}

        if "memory" not in data or not isinstance(data["memory"], list):
            data["memory"] = []

        return data

    except (json.JSONDecodeError, OSError):
        return {"memory": []}


def save_memory(data):
    """
    Save the complete memory structure.
    """

    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        return True

    except OSError:
        return False


def remember(key, value):
    """
    Add a new memory or update an existing memory.
    """

    data = load_memory()
    memories = data["memory"]

    # Update an existing key
    for item in memories:
        if item.get("key") == key:
            item["value"] = value
            return save_memory(data)

    # Add a new key
    memories.append({
        "key": key,
        "value": value
    })

    return save_memory(data)


def get_memory(key):
    """
    Retrieve a memory value using its key.
    """

    data = load_memory()

    for item in data["memory"]:
        if item.get("key") == key:
            return item.get("value")

    return None


def forget_memory(key):
    """
    Delete one memory using its key.
    """

    data = load_memory()
    memories = data["memory"]

    for index, item in enumerate(memories):
        if item.get("key") == key:
            del memories[index]
            return save_memory(data)

    return False