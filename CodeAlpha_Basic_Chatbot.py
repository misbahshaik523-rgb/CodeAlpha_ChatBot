def get_bot_response(user_input):
    """Takes user input and returns a predefined rule-based response."""
    user_input = user_input.strip().lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hi! Nice to meet you!"
    elif "how are you" in user_input:
        return "I'm fine, thanks! How are you?"
    elif "what is your name" in user_input or "your name" in user_input:
        return "I'm a simple Python chatbot."
    elif "who are you" in user_input:
        return "I am a rule-based chatbot created using Python."
    elif "help" in user_input:
        return "You can say hello, ask how I am, ask my name, or say bye."
    elif "thank" in user_input:
        return "You're welcome!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that. Try saying hello, asking how I am, or saying bye."


def chatbot():
    print("===== Basic Python Chatbot =====")
    print("Type 'bye' or 'goodbye' to exit.")
    print()

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("Bot:", response)

        if "bye" in user_input.strip().lower() or "goodbye" in user_input.strip().lower():
            break


if __name__ == "__main__":
    chatbot()
