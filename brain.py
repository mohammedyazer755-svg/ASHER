from config import username
from config import age , mom
from memory import get_memory , remember
from history import load_history , save_history , add_chat , show_history, clear_history
from commands import command_map
from utils import speak
from patterns import memory_patterns, memory_question
from nlu import process_memory
from conversations import handle_conversations
from search import search_memory


def greet():
    print(f"\nHello  {username}!")
    print("I am Asher")
    print("Version 0.1")
    print("Ready to assist you.\n")
   

def goodbye():
    print(f"\nGood Bye {username} machan")
    print("See you again")


def respond(user_input):
    key, val = search_memory(user_input)
    if val:
        speak(f"I remember that your {key} is {val}")
        return
    
    key, value = process_memory(user_input)
    if key:
        speak(f"I'll remember that your {key.lower()} is {value.lower()}.")
        return

    user_input = user_input.lower().strip()

    if handle_conversations(user_input):
        return

    for pattern , key in memory_patterns.items():
        if user_input.startswith(pattern):
            value = user_input.replace(pattern,"").strip()
            remember(key,value)
            speak(f"I'll remember your favourite {key.replace('_',' ')}")
            return

    for questions , key in memory_question.items():
        if user_input == questions:
            value = get_memory(key)
            if value:
                speak(f"Your favourite {key.replace('_',' ').lower()} is {value}")    
            else:
                speak(f"I don't know your {key.replace('_',' ').lower()} yet.")
            return
        
    if user_input.startswith("remember "):
        text = user_input.replace("remember ","")
        if "=" in text:
            key, value = text.split("=",1)
            key = key.strip()
            value= value.strip()
            remember(key,value)
            speak(f"I'll remember that {key} is {value}")
        else:
            speak("Use this format. \n remember key = value")
        return 

    if user_input.startswith("what is "):
        key = user_input.replace("what is","").strip()
        value= get_memory(key)
        if value:
            speak(f"{key} is {value}")
        else:
            speak(f"i dont know {key} yet.")
        return
    
    if user_input.startswith("tell me "):
        key = user_input.replace("tell me","").strip()
        value= get_memory(key)
        if value:
            speak(f"{key} is {value}")
        else:
            speak(f"i dont know {key} yet.")
        
    if user_input in command_map:
        command_map[user_input]()
        return
    
    elif user_input == "what is your favourite food":
        food = get_memory("Food")
        if food:
            speak(f"My favourite food is {food}")
        else:
            speak("I don't know your favourite food.")

    elif user_input == "which college do i study":
        college = get_memory("College")
        if college: 
            speak(f"You study at {college}")
        else:
            speak("I don't know which college you study at.")

    elif user_input == "what is my favourite colour":
        colour = get_memory("Fav_Colour")
        if colour:
            speak(f"Your favourite colour is {colour}")
        else:
            speak("I don't know your favourite colour.")

    elif user_input == "what is my dream company":
        company = get_memory("Dream Company")
        if company :
            speak(f"Your dream company is {company}")
        else:
            speak("I don't know your dream company.")
    

    elif user_input == "what is my favourite movie":
        movie= get_memory("Movie")
        if movie:
            speak(f"Your favourite movie is {movie}")
        else:
            speak("I don't know your favourite movie yet.")

    elif user_input == "who is my trusted person":
        trusted_person = get_memory("Trusted_Person")
        if trusted_person:
            speak(f"Your trusted person is {trusted_person}")
        else:
            speak("I don't know your trusted person.")

    
    elif user_input.startswith("my favourite movie is"):
        movie = user_input.replace("my favourite movie is", "").strip()
        remember("Movie",movie)
        speak("I'll remember that.")
    

    elif user_input.startswith("my dream company is"):
        company = user_input.replace("my dream company is", "").strip()
        remember("Dream Company",company)
        speak("I'll remember that")
    
    
    elif user_input.startswith("i trust"):
        trusted_person = user_input.replace("i trust", "").strip()
        remember("Trusted_Person", trusted_person)
        speak("I'll remember that")
        
    elif user_input == "show history":
        print("\n")
        show_history()
    
    elif user_input == "clear history":
        clear_history()
        add_chat("System", "History cleared by user.")
        print("Asher: History cleared.")
    
    else :
        speak("I don't understand that yet")