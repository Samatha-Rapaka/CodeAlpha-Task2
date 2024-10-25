import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you!"]
    ],
    [
        r"how are you?",
        ["I'm just a bunch of code, but thanks for asking!", "Doing well, how about you?"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!"]
    ],
    [
        r"(.*)",
        ["Sorry, I don't understand that."]
    ]
]

# Create the chatbot
def chatbot():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
