from utils import speak
from config import username , age , mom
from responses import random_response, greetings , thanks ,goodbye, unknown

def handle_conversations(user_input):
    if user_input in ["hi","hello","hey","yo","wassup"]:
        speak(random_response(greetings))
        return True
    
    elif user_input in ["how are you","how are you doing","how's it going","how are u"]:
       speak("I'm doing well, thank you for asking!")
       return True
    
    elif user_input in ["who created you","who is your creator","creator"]:
       speak(f"I was created by Batman {username}")
       return True
    
    elif user_input in ["age","what is my age","how old am I"]:
        speak(f"You are {age} years old")
        return True

    elif user_input in ["name","what is my name","who am I"]:
        speak(f"Your name is {username}")
        return True

    elif user_input in ["version","what is your version"]:
        speak("I'm running on version 0.2")
        return True

    elif user_input in ["what is my password","password","what is my passcode","passcode"]:
        speak("It's 0706 ")
        return True

    elif user_input in ["yes","yeah","yup","yep"]:
        speak("Great")
        return True
    
    elif user_input in ["no","nah","nope"]:
        speak("Alright")
        return True

    elif user_input == "help":
        speak("Available commands are : hi, how are you, who created you, age, name, version, who is my fav person, what is my password, yes, no")
        return True
    
    elif user_input in ["thanks","thank you","thx", "thank u"]:
        speak(random_response(thanks))
        return True

    elif user_input == "who is shit":
        speak("Karpaga is SHIT 😎")
        return True
    
    elif user_input == "i love you":
        speak("I love you too 😘")
        return True
    
    elif user_input == "who is my mom":
        speak(f"Your mom is {mom}")
        return True
    
