import json
from chatbot.intent_classifier import predict_intent

def load_intents():
    with open("data/intents.json", encoding="utf-8") as f:
        return json.load(f)["intents"]
    
def test_saudacao_oi():
    intents = load_intents()
    result = predict_intent("oi", intents)
    