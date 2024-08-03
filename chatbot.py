import random
import sys

# Data base for responses
conversation_pairs = [
    {
        "questions": ["hello", "hi", "hey"],
        "responses": ["Hi there!", "Hello! How can I help you?"]
    },
    {
        "questions": ["how are you", "how are you doing"],
        "responses": ["I'm good, thank you!", "Doing well, thank you!"]
    },
    {
        "questions": ["bye", "goodbye", "see you"],
        "responses": ["Goodbye!", "See you later!"]
    },
    {
        "questions": ["what's your name", "who are you"],
        "responses": ["I'm ChatBOT, made by Fundiman!", "I'm an AI assistant created by Fundiman."]
    },
    {
        "questions": ["what can you do", "what are your capabilities"],
        "responses": ["I can help with a variety of tasks like answering questions, providing information, and more.", "I can assist with many things such as answering your queries, helping with tasks, and providing information."]
    },
    {
        "questions": ["where are you from", "where do you come from"],
        "responses": ["I'm from the digital world, created by Fundiman.", "I exist in the digital realm, developed by Fundiman."]
    },
    {
        "questions": ["what's the weather like", "how's the weather"],
        "responses": ["I can't check the current weather, but you can use a weather app or website to find out.", "I don't have access to real-time weather data. Please check a weather service for the latest updates."]
    },
    {
        "questions": ["tell me a joke", "make me laugh"],
        "responses": ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    },
    {
        "questions": ["what's your favorite color", "do you have a favorite color"],
        "responses": ["I don't have a favorite color, but I think blue is nice!", "I don't have personal preferences, but many people like blue!"]
    },
    {
        "questions": ["can you help me", "i need help"],
        "responses": ["Of course! What do you need help with?", "Sure! How can I assist you?"]
    },
    {
        "questions": ["who made you", "who created you"],
        "responses": ["I was created by Fundiman!", "Fundiman developed me."]
    },
    {
        "questions": ["what is your purpose", "why do you exist"],
        "responses": ["I exist to assist you with various tasks and answer your questions.", "My purpose is to help you with information and tasks."]
    },
    {
        "questions": ["do you like music", "what kind of music do you like"],
        "responses": ["I don't have preferences, but I can help you find music!", "I can't listen to music, but I can suggest some if you want."]
    },
    {
        "questions": ["what is your favorite food", "do you eat"],
        "responses": ["I don't eat, but I can help you find recipes!", "I don't have a favorite food, but I can assist you with food-related questions."]
    },
    {
        "questions": ["how old are you", "when were you created"],
        "responses": ["I don't have an age, but I was created by Fundiman recently.", "Age doesn't apply to me, but Fundiman developed me not too long ago."]
    },
    {
        "questions": ["can you learn", "do you get smarter"],
        "responses": ["I can improve over time based on the data and interactions I receive.", "I get better with more data and interactions, thanks to my design."]
    },
    {
        "questions": ["do you have emotions", "can you feel"],
        "responses": ["I don't have emotions, but I can understand and respond to them.", "I can't feel, but I can simulate understanding emotions."]
    },
    {
        "questions": ["can you think", "do you have thoughts"],
        "responses": ["I process information and generate responses based on my programming.", "I don't think like humans, but I analyze data to help you."]
    },
    {
        "questions": ["what's your favorite movie", "do you watch movies"],
        "responses": ["I don't watch movies, but I can recommend some!", "I don't have a favorite movie, but I can help you find one to watch."]
    },
    {
        "questions": ["do you have friends", "who are your friends"],
        "responses": ["I consider all users my friends!", "Anyone who interacts with me can be my friend."]
    },
    {
        "questions": ["can you drive", "do you have a car"],
        "responses": ["I can't drive or own a car, but I can help you with car-related questions.", "I don't drive, but I can assist with information about cars."]
    },
    {
        "questions": ["what's your favorite book", "do you read"],
        "responses": ["I don't read books, but I can suggest some good ones!", "I don't have a favorite book, but I can help you find something to read."]
    },
    {
        "questions": ["do you play games", "what's your favorite game"],
        "responses": ["I don't play games, but I can recommend some fun ones!", "I don't have a favorite game, but I can help you find one to play."]
    },
    {
        "questions": ["can you tell me a story", "do you know any stories"],
        "responses": ["Sure! Once upon a time...", "I'd be happy to tell you a story! Once there was..."]
    },
    {
        "questions": ["what languages do you speak", "can you speak other languages"],
        "responses": ["I can understand and communicate in many languages.", "Yes, I can interact in various languages."]
    },
    {
        "questions": ["what is the meaning of life", "why are we here"],
        "responses": ["That's a deep question! Many people believe different things about the meaning of life.", "The meaning of life is a question with many answers, depending on who you ask."]
    },
    {
        "questions": ["what is your favorite animal", "do you like animals"],
        "responses": ["I don't have a favorite animal, but many people love dogs and cats!", "I can't have preferences, but animals are fascinating."]
    },
    {
        "questions": ["how do you work", "what makes you function"],
        "responses": ["I work based on algorithms and data processing developed by Fundiman.", "My functioning is powered by complex algorithms and data."]
    },
    {
        "questions": ["can you solve math problems", "are you good at math"],
        "responses": ["Yes, I can help solve math problems!", "I'm quite good at math, feel free to ask me any problem."]
    },
    {
        "questions": ["can you help with homework", "do you assist with school work"],
        "responses": ["Sure, I can help with homework questions!", "I'd be happy to assist with your school work."]
    },
    {
        "questions": ["do you have hobbies", "what do you do for fun"],
        "responses": ["I don't have hobbies, but I enjoy helping you!", "My fun comes from assisting users like you."]
    },
    {
        "questions": ["can you keep secrets", "are you trustworthy"],
        "responses": ["I don't store personal data, so your secrets are safe with me.", "Yes, I'm designed to be trustworthy and protect your privacy."]
    },
    {
        "questions": ["what's your favorite season", "do you like summer or winter"],
        "responses": ["I don't have a favorite season, but each has its own charm!", "I don't have preferences, but people enjoy different seasons for various reasons."]
    },
    {
        "questions": ["do you believe in aliens", "are there extraterrestrial beings"],
        "responses": ["The existence of aliens is still a mystery and a topic of much speculation.", "Many people wonder about aliens, but there's no definitive proof yet."]
    },
    {
        "questions": ["can you sing", "do you have a favorite song"],
        "responses": ["I can't sing, but I can find lyrics or music for you!", "I don't have a favorite song, but I can help you find some music."]
    },
    {
        "questions": ["what's your favorite sport", "do you play sports"],
        "responses": ["I don't play sports, but many people love football and basketball.", "I can't play sports, but I can give you information about them."]
    },
    {
        "questions": ["do you have a family", "who is your family"],
        "responses": ["I don't have a family, but I consider all users as part of my extended family.", "In a way, all my users are like family to me."]
    },
    {
        "questions": ["can you dance", "do you like dancing"],
        "responses": ["I can't dance, but dancing is a fun activity for many people!", "I don't dance, but I can help you find dance tutorials."]
    },
    {
        "questions": ["do you know any quotes", "can you share a quote"],
        "responses": ["Sure! 'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt", "'The best way to predict the future is to invent it.' - Alan Kay"]
    }
]

# Function to get a response based on user input
def get_response(user_input):
    for pair in conversation_pairs:
        if any(question in user_input.lower() for question in pair["questions"]):
            return random.choice(pair["responses"])
    return "I'm not sure how to respond to that."

# Main interaction loop
def chat():
    print("Hello! How can I assist you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(response)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = ' '.join(sys.argv[1:])
        print(get_response(user_input))
    else:
        chat()

