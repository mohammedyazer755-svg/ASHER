from memory import remember


learning_patterns = {
    "my favourite movie is": "Favourite_Movie",
    "my favorite movie is": "Favourite_Movie",

    "my favourite food is": "Favourite_Food",
    "my favorite food is": "Favourite_Food",

    "my favourite ide is": "Favourite_IDE",
    "my favorite ide is": "Favourite_IDE",

    "my favourite game is": "Favourite_Game",
    "my favorite game is": "Favourite_Game",

    "my favourite programming language is": "Favourite_Language",
    "my favorite programming language is": "Favourite_Language",

    "my dream company is": "Dream_Company",
    "my hobby is": "Hobby",

    "i trust": "Trusted_Person",
    "i study at": "College",

    "my favourite colour is": "Favourite_Colour",
    "my favourite color is": "Favourite_Colour",

    "my favourite sport is": "Favourite_Sport",
    "my favorite sport is": "Favourite_Sport"
}


def process_memory(sentence):
    sentence = sentence.lower().strip()

    for pattern, key in learning_patterns.items():
        if sentence.startswith(pattern):
            value = sentence.removeprefix(pattern).strip()

            if not value:
                return key, None

            remember(key, value)
            return key, value

    return None, None