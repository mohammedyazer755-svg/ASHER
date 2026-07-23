from utils import speak
from config import username , age

def hello():
    speak("Hello !")

def show_name():
    speak(f"Your name is {username}")

def show_age():
    speak(f"You are {age} years old")

def show_version():
    speak("I'm running on version 0.2")

def help():
    speak("How can i help you sir ?")

def creator():
    speak(f"I was created by Batman{username}")

def thank():
    speak("You're welcome!")

def commands():
    speak("Available commands are : hi, how are you, who created you, age, name, version, who is my fav person, what is my password, yes, no")

command_map ={
    "hi" : hello,
    "hello" : hello,
    "name" : show_name,
    "age" : show_age,
    "version" : show_version,
    "help" : help,
    "creator" : creator,
    "thanks" : thank,
    "commands": commands
}