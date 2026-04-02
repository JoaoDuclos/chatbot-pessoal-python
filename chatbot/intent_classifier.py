from chatbot.nlp import preprocess

def predict_intent(user_input, intents):
    user_words = set(preprocess(user_input))

    best_intent = None
    best_match_percent = 0.0
    fallback_intent = None
    THRESHOLD = 0.5

    for intent in intents:
        if intent["tag"] == "conversa_padrao":
            fallback_intent = intent
            continue

        for pattern in intent["patterns"]:
            pattern_words = set(preprocess(pattern))

            common_words = user_words & pattern_words
            match_percent = len(common_words) / len(pattern_words)

            if match_percent > best_match_percent:
                best_match_percent = match_percent
                best_intent = intent

    if best_match_percent >= THRESHOLD:
        return best_intent

    return fallback_intent

        
