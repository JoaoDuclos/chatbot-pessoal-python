
from chatbot.chatbot import Chatbot


def main():
    bot = Chatbot("data/intents.json")
    print("🤖 Chatbot iniciado! Digite 'sair' para encerrar.\n")

    while True:
        user_input = input("Você: ")

        if user_input.lower() == "sair":
            print("Bot: Até logo! 👋")
            break

        response = bot.get_response(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
