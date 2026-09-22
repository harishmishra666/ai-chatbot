def chatbot():
    print("🤖 AI Chatbot")
    print("Type 'bye' to exit.")
    print()

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hello! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        elif user_input == "what is ai":
            print("Bot: AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.")

        elif user_input == "what is python":
            print("Bot: Python is a popular programming language used in AI, automation, data science, and software development.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day 👋")
            break

        else:
            print("Bot: Sorry, I don't understand that yet.")


if __name__ == "__main__":
    chatbot()
