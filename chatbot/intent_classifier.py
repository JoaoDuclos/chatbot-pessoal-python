from chatbot.nlp import preprocess #lembrar colocar apenas nlp para testes
import json

def predict_intent(user_input, intents):
    user_words = set(preprocess(user_input))

    best_intent = None
    best_match_percent = 0.0
    fallback_intent = None
    THRESHOLD = 0.1

    for intent in intents:
        if intent["tag"] == "conversa_padrao":
            fallback_intent = intent
            continue
        pattern_words = set()

        for pattern in intent['patterns']:
            pattern_words.update(preprocess(pattern))
        
        #achei o problema, eu vou ter que criar um for (ou encontrar uma forma mais eficiente) para que todas as palavras da pattern sejam preprocessadas

        common_words = user_words & pattern_words
        match_percent = len(common_words) / len(pattern_words)

        if match_percent > best_match_percent:
            best_match_percent = match_percent
            best_intent = intent

    if best_match_percent >= THRESHOLD:
        return best_intent
        # para testes no próprio arquivo
        #return [best_intent, best_match_percent]
    return fallback_intent
    # para testes no próprio arquivo
    #return [fallback_intent, best_match_percent]

# para testes no próprio arquivo

#with open("data/intents.json", encoding="utf-8") as file:
#    data = json.load(file)
#    intents = data["intents"]

# user_input = 'quem é você?'
# print(predict_intent(user_input, intents))