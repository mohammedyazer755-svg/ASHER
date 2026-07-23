from brain import greet, goodbye , respond
from history import add_chat

print("=========================")
print("         ASHER V01       ")
print("=========================")
greet()
while True :
    user = input("YOU :")
    add_chat("You", user)
    
    if user.lower() in ["bye", "tata", "goodbye", "exit", "quit"]:
        goodbye()
        break
    respond(user)
    print("\n")
