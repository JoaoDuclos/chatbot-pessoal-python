import random
import json


class Chatbot:
    def __init__(self, intents_path):
        with open(intents_path, encoding="utf-8") as file:
            data = json.load(file)
            self.intents = data["intents"]

    def get_response(self, user_input):
        user_input = user_input.lower()

        for intent in self.intents:
            for pattern in intent["patterns"]:
                if pattern in user_input:
                    return random.choice(intent["responses"])

        # fallback
        fallback_intent = next(
            intent for intent in self.intents if intent["tag"] == "conversa_padrao"
        )
        return random.choice(fallback_intent["responses"])
