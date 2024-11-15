import spacy
import random

nlp = spacy.load("en_core_web_sm")

responses = {
    "greeting": ["Hello!", "Hi, how can I assist you?", "Hey there!", "Hello! How's it going?"],
    "feeling": ["I'm sorry to hear that. Do you want to talk about it?", "That sounds great!", "Why do you feel that way?", "I hope things get better soon!"],
    "farewell": ["Goodbye! Take care!", "Talk to you later!", "Have a great day!", "See you next time!"],
    "help": ["I'm here to help! What do you need assistance with?", "How can I assist you today?", "Feel free to ask me anything!", "I'm happy to help! Just let me know what you need."],
    "bot_info": ["I'm a simple chatbot created to have conversations with you.", "I can assist you with various things like answering questions, having a chat, or even helping you with some simple tasks!", "I'm here to chat and help with anything I can!"],
    "time_related": ["I'm not great at keeping track of time, but it's always a good time to chat!", "I can't check the time right now, but I hope you're enjoying your day!", "No matter the time, I'm here for you!"],
    "default": ["Hmm, that's interesting. What else?", "Can you tell me more?", "That's something I haven't thought about!", "I'm not sure about that, but I'm always learning."]
}

class Chatbot:
    def __init__(self):
        self.context = {"mood": None, "topic": None}
        self.nlp = spacy.load("en_core_web_sm")
    
    def analyze_input(self, user_input):
        doc = self.nlp(user_input)
        
        
        for token in doc:
            if token.lemma_ in ["hi", "hello", "hey"]:
                return random.choice(responses["greeting"])
            elif token.lemma_ in ["bye", "goodbye", "farewell"]:
                return random.choice(responses["farewell"]) 
        
        # Check for mood-related
        for token in doc:
            if token.lemma_ in ["sad", "happy", "angry"]:
                self.context["mood"] = token.text
                return f"I see that you're feeling {token.text}. Do you want to talk more about it?"

        # checks if user need help
        for token in doc:
            if token.lemma_ in ["help", "assist", "support"]:
                return random.choice(responses["help"])

        # Check if user is asking about the chatbot
        if "who" in user_input.lower() and "you" in user_input.lower():
            return random.choice(responses["bot_info"])

        # Check for time-related
        if "time" in user_input.lower() or "day" in user_input.lower():
            return random.choice(responses["time_related"])
        
    
        return random.choice(responses["default"])

    def run(self):
        print("Chatbot: Hi there! How can I help you today? (Type 'exit' to quit)")

        while True:
            user_input = input("You: ")

            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break

            response = self.analyze_input(user_input)
            print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    bot = Chatbot()
    bot.run()
