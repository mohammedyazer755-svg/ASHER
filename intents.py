memory_intents = {
    "Favourite_Movie": [
        ["favourite", "movie"],
        ["favorite", "movie"],
        ["movie", "like"]
    ],

    "Favourite_Food": [
        ["favourite", "food"],
        ["favorite", "food"],
        ["food", "like"]
    ],

    "Favourite_IDE": [
        ["favourite", "ide"],
        ["favorite", "ide"],
        ["ide", "use"],
        ["coding", "editor"]
    ],

    "Favourite_Game": [
        ["favourite", "game"],
        ["favorite", "game"],
        ["game", "like"]
    ],

    "Favourite_Language": [
        ["favourite", "programming", "language"],
        ["favorite", "programming", "language"],
        ["language", "code"],
        ["coding", "language"]
    ],

    "Dream_Company": [
        ["dream", "company"],
        ["company", "work"],
        ["target", "company"]
    ],

    "Hobby": [
        ["my", "hobby"],
        ["what", "enjoy"]
    ],

    "Trusted_Person": [
        ["trusted", "person"],
        ["who", "trust"]
    ],

    "College": [
        ["which", "college"],
        ["where", "study"]
    ]
}


display_names = {
    "Favourite_Movie": "favourite movie",
    "Favourite_Food": "favourite food",
    "Favourite_IDE": "favourite IDE",
    "Favourite_Game": "favourite game",
    "Favourite_Language": "favourite programming language",
    "Dream_Company": "dream company",
    "Hobby": "hobby",
    "Trusted_Person": "trusted person",
    "College": "college"
}


def detect_memory_intent(sentence):
    sentence = sentence.lower().strip()

    for memory_key, keyword_groups in memory_intents.items():
        for keywords in keyword_groups:
            if all(word in sentence for word in keywords):
                return memory_key

    return None