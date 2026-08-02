from config import username
from memory import get_memory, remember, forget_memory
from history import add_chat, show_history, clear_history
from commands import command_map
from utils import speak
from nlu import process_memory
from conversations import handle_conversations
from search import search_memory
from intents import detect_memory_intent, display_names
from deletion import detect_delete_intent


# --------------------------------------------------
# TEMPORARY CONVERSATION CONTEXT
# --------------------------------------------------

last_memory_key = None
pending_memory_key = None

pending_update_key = None
pending_update_value = None

pending_delete_key = None


# --------------------------------------------------
# STARTUP AND EXIT
# --------------------------------------------------

def greet():
    print(f"\nHello {username}!")
    print("I am Asher")
    print("Version 0.1")
    print("Ready to assist you.\n")


def goodbye():
    print(f"\nGoodbye {username}, machan!")
    print("See you again.")


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def get_display_name(key):
    """
    Convert an internal memory key into a readable name.

    Example:
    Favourite_Movie -> favourite movie
    Favourite_IDE   -> favourite IDE
    """

    return display_names.get(
        key,
        key.replace("_", " ").lower()
    )


def update_context_memory(new_value):
    """
    Propose an update for the most recently discussed memory.
    """

    global last_memory_key
    global pending_update_key, pending_update_value

    if not last_memory_key:
        speak("I'm not sure what you want me to change.")
        return False

    new_value = new_value.strip()

    if not new_value:
        speak("Please tell me the new value.")
        return False

    old_value = get_memory(last_memory_key)
    name = get_display_name(last_memory_key)

    # The proposed value is already stored
    if old_value and old_value.lower() == new_value.lower():
        speak(f"Your {name} is already {old_value}.")
        return False

    # Existing value found — ask before replacing
    if old_value:
        pending_update_key = last_memory_key
        pending_update_value = new_value

        speak(
            f"Your {name} is currently {old_value}. "
            f"Should I change it to {new_value}?"
        )
        return True

    # No existing value — save directly
    remember(last_memory_key, new_value)

    speak(f"I changed your {name} to {new_value}.")
    return True


# --------------------------------------------------
# MAIN RESPONSE FUNCTION
# --------------------------------------------------

def respond(user_input):
    global last_memory_key, pending_memory_key
    global pending_update_key, pending_update_value
    global pending_delete_key

    # Preserve original capitalization
    original_input = user_input.strip()
    user_input = original_input.lower()

    confirmation_words = {
        "yes",
        "yeah",
        "yup",
        "yep",
        "sure",
        "confirm",
        "do it",
        "okay",
        "ok",
        "correct",
        "proceed"
    }

    rejection_words = {
        "no",
        "nope",
        "cancel",
        "don't",
        "do not",
        "leave it",
        "let it be",
        "keep old",
        "keep it",
        "not now",
        "cancel update",
        "don't delete it",
        "do not delete it"
    }

    cancel_words = {
        "cancel",
        "never mind",
        "nevermind",
        "stop",
        "skip"
    }

    # --------------------------------------------------
    # 1. EMPTY INPUT
    # --------------------------------------------------

    if not user_input:
        if pending_delete_key:
            speak("Please answer yes or no.")

        elif pending_update_key:
            speak("Please answer yes or no.")

        elif pending_memory_key:
            name = get_display_name(pending_memory_key)
            speak(f"Please tell me your {name}.")

        else:
            speak("Please type something.")

        return

    # --------------------------------------------------
    # 2. CONFIRM OR REJECT MEMORY DELETION
    # --------------------------------------------------

    if pending_delete_key:
        if user_input in confirmation_words:
            key = pending_delete_key
            name = get_display_name(key)

            deleted = forget_memory(key)

            pending_delete_key = None

            if deleted:
                # Clear related temporary context
                if last_memory_key == key:
                    last_memory_key = None

                pending_memory_key = None
                pending_update_key = None
                pending_update_value = None

                speak(f"I forgot your {name}.")
            else:
                speak(f"I couldn't find your {name} in memory.")

            return

        if user_input in rejection_words:
            name = get_display_name(pending_delete_key)

            pending_delete_key = None

            speak(f"Okay, I kept your {name}.")
            return

        speak("Please answer yes or no.")
        return

    # --------------------------------------------------
    # 3. CONFIRM OR REJECT MEMORY UPDATE
    # --------------------------------------------------

    if pending_update_key:
        if user_input in confirmation_words:
            key = pending_update_key
            new_value = pending_update_value

            remember(key, new_value)

            name = get_display_name(key)
            last_memory_key = key

            pending_update_key = None
            pending_update_value = None

            speak(f"I changed your {name} to {new_value}.")
            return

        if user_input in rejection_words:
            name = get_display_name(pending_update_key)

            pending_update_key = None
            pending_update_value = None

            speak(f"Okay, I kept your existing {name}.")
            return

        speak("Please answer yes or no.")
        return

    # --------------------------------------------------
    # 4. CANCEL PENDING MEMORY REQUEST
    # --------------------------------------------------

    if pending_memory_key and user_input in cancel_words:
        pending_memory_key = None

        speak("Okay, I cancelled it.")
        return

    # --------------------------------------------------
    # 5. CAPTURE PENDING MEMORY VALUE
    # --------------------------------------------------

    if pending_memory_key:
        key = pending_memory_key
        value = original_input

        old_value = get_memory(key)
        name = get_display_name(key)

        pending_memory_key = None

        # Different value already exists
        if old_value and old_value.lower() != value.lower():
            pending_update_key = key
            pending_update_value = value

            speak(
                f"Your {name} is currently {old_value}. "
                f"Should I change it to {value}?"
            )
            return

        # Same value already exists
        if old_value and old_value.lower() == value.lower():
            last_memory_key = key

            speak(
                f"I already remember that your "
                f"{name} is {old_value}."
            )
            return

        # New value
        remember(key, value)

        last_memory_key = key

        speak(f"I'll remember that your {name} is {value}.")
        return

    # --------------------------------------------------
    # 6. CONTEXT-BASED MEMORY DELETION
    # --------------------------------------------------

    if user_input in {
        "forget it",
        "delete it",
        "remove it"
    }:
        if not last_memory_key:
            speak("I'm not sure what you want me to forget.")
            return

        old_value = get_memory(last_memory_key)
        name = get_display_name(last_memory_key)

        if not old_value:
            speak(f"I don't have your {name} stored.")
            return

        pending_memory_key = None
        pending_update_key = None
        pending_update_value = None

        pending_delete_key = last_memory_key

        speak(
            f"Should I forget that your "
            f"{name} is {old_value}?"
        )
        return

    # --------------------------------------------------
    # 7. DETECT DIRECT MEMORY DELETION REQUEST
    # --------------------------------------------------

    delete_key = detect_delete_intent(user_input)

    if delete_key:
        old_value = get_memory(delete_key)
        name = get_display_name(delete_key)

        if not old_value:
            speak(f"I don't have your {name} stored.")
            return

        # Prevent conflicting pending actions
        pending_memory_key = None
        pending_update_key = None
        pending_update_value = None

        pending_delete_key = delete_key

        speak(
            f"Should I forget that your "
            f"{name} is {old_value}?"
        )
        return

    # --------------------------------------------------
    # 8. LEARN NEW INFORMATION
    # --------------------------------------------------

    key, value = process_memory(
        user_input,
        original_input
    )

    if key:
        name = get_display_name(key)

        # Pattern detected, but value is missing
        if not value:
            pending_memory_key = key

            speak(f"Please tell me your {name}.")
            return

        old_value = get_memory(key)

        # Different value already exists
        if old_value and old_value.lower() != value.lower():
            pending_update_key = key
            pending_update_value = value

            speak(
                f"Your {name} is currently {old_value}. "
                f"Should I change it to {value}?"
            )
            return

        # Same value already exists
        if old_value and old_value.lower() == value.lower():
            last_memory_key = key

            speak(
                f"I already remember that your "
                f"{name} is {old_value}."
            )
            return

        # New memory
        remember(key, value)

        last_memory_key = key
        pending_memory_key = None

        speak(f"I'll remember that your {name} is {value}.")
        return

    # --------------------------------------------------
    # 9. FOLLOW-UP CONTEXT UPDATES
    # --------------------------------------------------

    if user_input.startswith("change it to "):
        new_value = original_input[len("change it to "):].strip()
        update_context_memory(new_value)
        return

    if user_input.startswith("set it as "):
        new_value = original_input[len("set it as "):].strip()
        update_context_memory(new_value)
        return

    if user_input.startswith("make it "):
        new_value = original_input[len("make it "):].strip()
        update_context_memory(new_value)
        return

    if user_input.startswith("actually, it is "):
        new_value = original_input[len("actually, it is "):].strip()
        update_context_memory(new_value)
        return

    if user_input.startswith("actually it is "):
        new_value = original_input[len("actually it is "):].strip()
        update_context_memory(new_value)
        return

    # --------------------------------------------------
    # 10. CLEAR CONVERSATION CONTEXT
    # --------------------------------------------------

    if user_input == "clear context":
        last_memory_key = None
        pending_memory_key = None

        pending_update_key = None
        pending_update_value = None

        pending_delete_key = None

        speak("Conversation context cleared.")
        return

    # --------------------------------------------------
    # 11. DETECT MEMORY QUESTIONS
    # --------------------------------------------------

    memory_key, confidence, tied_intents = detect_memory_intent(
        user_input
    )

    if tied_intents:
        names = [
            get_display_name(intent)
            for intent in tied_intents
        ]

        options = " or ".join(names)

        speak(f"Did you mean {options}?")
        return

    if memory_key:
        last_memory_key = memory_key

        value = get_memory(memory_key)
        name = get_display_name(memory_key)

        if value:
            speak(f"Your {name} is {value}.")
        else:
            speak(f"I don't know your {name} yet.")

        return

    # --------------------------------------------------
    # 12. MANUAL MEMORY COMMAND
    # --------------------------------------------------

    if user_input.startswith("remember "):
        text = original_input[len("remember "):].strip()

        if "=" not in text:
            speak("Use this format: remember key = value")
            return

        key, value = text.split("=", 1)

        key = key.strip()
        value = value.strip()

        if not key or not value:
            speak("Both the memory name and value are required.")
            return

        old_value = get_memory(key)

        if old_value and old_value.lower() != value.lower():
            pending_update_key = key
            pending_update_value = value

            name = get_display_name(key)

            speak(
                f"{name} is currently {old_value}. "
                f"Should I change it to {value}?"
            )
            return

        if old_value and old_value.lower() == value.lower():
            name = get_display_name(key)
            last_memory_key = key

            speak(
                f"I already remember that your "
                f"{name} is {old_value}."
            )
            return

        remember(key, value)
        last_memory_key = key

        speak(f"I'll remember that {key} is {value}.")
        return

    # --------------------------------------------------
    # 13. GENERIC MEMORY RETRIEVAL
    # --------------------------------------------------

    if user_input.startswith("what is "):
        key = original_input[len("what is "):].strip()
        value = get_memory(key)

        if value:
            speak(f"{key} is {value}.")
        else:
            speak(f"I don't know {key} yet.")

        return

    if user_input.startswith("tell me "):
        key = original_input[len("tell me "):].strip()
        value = get_memory(key)

        if value:
            speak(f"{key} is {value}.")
        else:
            speak(f"I don't know {key} yet.")

        return

    # --------------------------------------------------
    # 14. HISTORY COMMANDS
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
    # 15. OTHER COMMANDS
    # --------------------------------------------------

    if user_input in command_map:
        command_map[user_input]()
        return

    # --------------------------------------------------
    # 16. CASUAL CONVERSATION
    # --------------------------------------------------

    if handle_conversations(user_input):
        return

    # --------------------------------------------------
    # 17. CONTROLLED FUZZY MEMORY SEARCH
    # --------------------------------------------------

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
            last_memory_key = key

            speak(f"I remember that your {name} is {value}.")
        else:
            speak("I couldn't find a matching memory.")

        return

    # --------------------------------------------------
    # 18. UNKNOWN INPUT
    # --------------------------------------------------

    speak("I don't understand that yet.")