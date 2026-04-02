from chatbot.nlp import preprocess

def predict_intent(user_input, intents):
    user_words = set(preprocess(user_input))

    best_intent = None
    best_score = 0
    
    for intent in intents:
        score = 0
        for pattern in intent["patterns"]:
            pattern_words = set(preprocess(pattern))
            score += len(user_words & pattern_words)

        if score > best_score:
            best_score = score
            best_intent = intent

    return best_intent

        
