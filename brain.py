from config import username
from memory import get_memory, remember
from history import add_chat, show_history, clear_history
from commands import command_map
from utils import speak
from nlu import process_memory
from conversations import handle_conversations
from search import search_memory
from intents import detect_memory_intent, display_names


def greet():
    print(f"\nHello {username}!")
    print("I am Asher")
    print("Version 0.1")
    print("Ready to assist you.\n")


def goodbye():
    print(f"\nGoodbye {username}, machan!")
    print("See you again.")


def get_display_name(key):
    """
    Converts internal memory keys into natural display names.

    Example:
    Favourite_Movie -> favourite movie
    Favourite_IDE   -> favourite IDE
    """

    return display_names.get(
        key,
        key.replace("_", " ").lower()
    )


def respond(user_input):

    # Clean the input before processing it
    user_input = user_input.lower().strip()

    if not user_input:
        speak("Please type something.")
        return

    # --------------------------------------------------
    # 1. LEARN NEW INFORMATION
    # --------------------------------------------------

    # Example:
    # "my favourite movie is bigil"
    key, value = process_memory(user_input)

    if key :
        name = get_display_name(key)
        if value :
             speak(f"I'll remember that your {name} is {value}.")
        else:
            speak(f"Please tell me your {name}.")
        return 

    # --------------------------------------------------
    # 2. DETECT MEMORY QUESTIONS
    # --------------------------------------------------

    # Example:
    # "what is my favourite movie?"
    # "which movie do I like?"
    memory_key, confidence, tied_intents = detect_memory_intent(user_input)
    if tied_intents:
       names = [
           get_display_name(intent)
           for intent in tied_intents
    ]

       options = " or ".join(names)

       speak(f"Did you mean {options}?")
       return
    
    if memory_key:
        value = get_memory(memory_key)
        name = get_display_name(memory_key)

        if value:
            speak(f"Your {name} is {value}.")
        else:
            speak(f"I don't know your {name} yet.")

        return

    # --------------------------------------------------
    # 3. MANUAL MEMORY COMMAND
    # --------------------------------------------------

    # Format:
    # remember key = value
    if user_input.startswith("remember "):
        text = user_input.removeprefix("remember ").strip()

        if "=" not in text:
            speak("Use this format: remember key = value")
            return

        key, value = text.split("=", 1)

        key = key.strip()
        value = value.strip()

        if not key or not value:
            speak("Both the memory name and value are required.")
            return

        remember(key, value)
        speak(f"I'll remember that {key} is {value}.")
        return

    # --------------------------------------------------
    # 4. GENERIC MEMORY RETRIEVAL
    # --------------------------------------------------

    # Example:
    # "what is hobby"
    if user_input.startswith("what is "):
        key = user_input.removeprefix("what is ").strip()
        value = get_memory(key)

        if value:
            speak(f"{key} is {value}.")
        else:
            speak(f"I don't know {key} yet.")

        return

    # Example:
    # "tell me hobby"
    if user_input.startswith("tell me "):
        key = user_input.removeprefix("tell me ").strip()
        value = get_memory(key)

        if value:
            speak(f"{key} is {value}.")
        else:
            speak(f"I don't know {key} yet.")

        return

    # --------------------------------------------------
    # 5. HISTORY COMMANDS
    # --------------------------------------------------

    if user_input == "show history":
        print()
        show_history()
        return

    if user_input == "clear history":
        clear_history()
        add_chat("System", "History cleared by user.")
        speak("History cleared.")
        return

    # --------------------------------------------------
    # 6. OTHER COMMANDS
    # --------------------------------------------------

    if user_input in command_map:
        command_map[user_input]()
        return

    # --------------------------------------------------
    # 7. CASUAL CONVERSATION
    # --------------------------------------------------

    # Example:
    # hi, hello, thanks, bye
    if handle_conversations(user_input):
        return

    # --------------------------------------------------
    # 8. CONTROLLED FUZZY MEMORY SEARCH
    # --------------------------------------------------

    # Fuzzy search is only used for clear memory questions.
    # This prevents statements such as:
    # "my favourite movie is bigil"
    # from retrieving an old movie value.
    memory_search_phrases = (
        "do you remember",
        "search memory",
        "remember my",
        "can you remember"
    )

    if user_input.startswith(memory_search_phrases):
        key, value = search_memory(user_input)

        if key and value:
            name = get_display_name(key)
            speak(f"I remember that your {name} is {value}.")
        else:
            speak("I couldn't find a matching memory.")

        return

    # --------------------------------------------------
    # 9. UNKNOWN INPUT
    # --------------------------------------------------

    speak("I don't understand that yet.")