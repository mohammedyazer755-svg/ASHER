from memory import remember

def process_memory(sentance):
    patterns = {
    "i study at" : "College",
    "my hobby is" : "hobby",
    "i trust" : "Trusted_Person",
    "my favourite bike is" : "Bike",
    "my favourite game is" : "Game",
    "my favourite language is" : "Language",
    "my favourite ide is" : "IDE",
    "my favourite os is": "operating_system"
}
    
    for pattern , key in patterns.items():
        if sentance.startswith(pattern):
            value = sentance.replace(pattern ,"").strip()
            remember(key,value)
            return key,value
        
    return None, None



