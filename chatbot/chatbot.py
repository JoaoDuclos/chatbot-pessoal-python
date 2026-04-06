import random
import json
from chatbot.intent_classifier import predict_intent


class Chatbot:
    def __init__(self, intents_path):
        with open(intents_path, encoding="utf-8") as file:
            data = json.load(file)
            self.intents = data["intents"]

    def get_response(self, user_input):
        
        intent = predict_intent(user_input, self.intents)
        return random.choice(intent["responses"])
