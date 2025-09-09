print("🤖 Chatbot is running! Type 'bye' to quit.\n")
while True:
    user_input = input("You: ").lower() 
    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you today?")
    elif "how are you" in user_input:
        print("Bot: I'm just a bot, but I'm doing great! Thanks for asking")
    elif "your name" in user_input:
        print("Bot: I'm your friendly Python Chatbot!")
    elif "time" in user_input:
        from datetime import datetime
        print("Bot: Current time is " + datetime.now().strftime("%H:%M:%S"))
    elif "bye" in user_input:
        print("Bot: Goodbye 👋 Have a great day!")
        break
    else:
        print("Bot: Sorry, I don’t understand that yet 🤔")
