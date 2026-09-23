def chatbot():
    print("🤖 AI Chatbot")
    print("Type 'bye' to exit.")
    print()

    while True:
        user_input = input("You: ").lower().strip()

        # Greetings
        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you?")

        # How are you
        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking.")

        # Artificial Intelligence
        elif (
            "what is ai" in user_input
            or "what is artificial intelligence" in user_input
            or "ai kya hai" in user_input
            or "artificial intelligence kya hai" in user_input
        ):
            print("Bot: AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.")

        # Python
        elif "what is python" in user_input or "python" in user_input:
            print("Bot: Python is a popular programming language used in AI, automation, data science, and software development.")

        # Sri Ram Swaroop
        elif "sri ram swaroop" in user_input or "sriramswaroop" in user_input:
            print("Bot: Sri Ram Swaroop Memorial College is an educational institution that offers academic and professional programs.")

        # Machine Learning
        elif "what is machine learning" in user_input or "machine learning" in user_input:
            print("Bot: Machine Learning is a branch of AI that enables computers to learn patterns from data and make predictions or decisions.")

        # Generative AI
        elif "what is generative ai" in user_input or "generative ai" in user_input:
            print("Bot: Generative AI is a type of AI that can generate new content such as text, images, audio, video, and code.")

        # Automation
        elif "what is automation" in user_input or "automation" in user_input:
            print("Bot: Automation uses technology to perform tasks automatically with minimal human intervention.")

        # Exit
        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day 👋")
            break

        # Unknown question
        else:
            print("Bot: Sorry, I don't understand that yet.")


if __name__ == "__main__":
    chatbot()