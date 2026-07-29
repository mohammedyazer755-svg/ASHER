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
        ["what", "hobby"],
        ["what", "enjoy"],
        ["do", "for", "fun"]
    ],

    "Trusted_Person": [
        ["trusted", "person"],
        ["who", "trust"],
        ["person", "trust"]
    ],

    "College": [
        ["which", "college"],
        ["where", "study"],
        ["college", "study"]
    ],

    "Favourite_Colour": [
        ["favourite", "colour"],
        ["favorite", "color"],
        ["colour", "like"],
        ["color", "like"]
    ],

    "Favourite_Sport": [
        ["favourite", "sport"],
        ["favorite", "sport"],
        ["sport", "like"]
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
    "College": "college",
    "Favourite_Colour": "favourite colour",
    "Favourite_Sport": "favourite sport"
}


def detect_memory_intent(sentence, minimum_confidence=0.6):
    sentence = sentence.lower().strip()

    words = (
        sentence
        .replace("?", "")
        .replace(".", "")
        .replace(",", "")
        .replace("!", "")
        .split()
    )

    best_intent = None
    best_score = 0.0

    for memory_key, keyword_groups in memory_intents.items():

        for keywords in keyword_groups:
            matched_keywords = 0

            for keyword in keywords:
                if keyword in words:
                    matched_keywords += 1

            score = matched_keywords / len(keywords)

            if score > best_score:
                best_score = score
                best_intent = memory_key

    if best_score >= minimum_confidence:
        return best_intent, best_score

    return None, best_score