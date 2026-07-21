print("Simple Chatbot")
print("Type 'Bye' to exit")
while True:
    user = input("You: ").lower()
    if user == "hello":
        print("Bot: Hi!")
    elif user == "how are you":
        print("Bot: I am fine, thank you!")
    elif user == "what is your name":
        print("Bot: My name is ChatBot.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: sorry, I don't understand.")
        