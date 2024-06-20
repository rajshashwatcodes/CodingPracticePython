import random

class ChatBot:
    def __init__(self):
        self.responses = {
            "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
            "how are you": ["I'm a chatbot, so I don't have feelings, but I'm here to help you!", "I'm just a bunch of code, but I'm ready to assist you!"],
            "what is your name": ["I am ChatBot, your virtual assistant.", "You can call me ChatBot."],
            "bye": ["Goodbye!", "See you later!", "Have a great day!"],
            "default": ["I'm not sure how to respond to that.", "Can you rephrase that?", "I don't understand."]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])

def main():
    bot = ChatBot()
    print("ChatBot: Hi! I'm your friendly chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = bot.get_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()
