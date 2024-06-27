import numpy as np
from keras.models import load_model
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import random
import json

# Load intents from the JSON file
with open("intents.json", "r") as file:
    intents = json.load(file)["intents"]

# Load the saved model and preprocessing objects
model = load_model('novamodel.keras')
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
lemmatizer = WordNetLemmatizer()

# Function to process user input and generate a response
def get_response(user_input):
    # Tokenize and lemmatize user input
    input_words = nltk.word_tokenize(user_input)
    input_words = [lemmatizer.lemmatize(word.lower()) for word in input_words]

    # Create a bag of words representation for the input
    bag = [0] * len(words)
    for word in input_words:
        if word in words:
            bag[words.index(word)] = 1

    # Make predictions using the trained model
    results = model.predict(np.array([bag]))
    # Get the index of the predicted class
    predicted_class_index = np.argmax(results)
    # Get the predicted class label
    predicted_class = classes[predicted_class_index]

    # Find the appropriate response for the predicted class
    for intent in intents:
        if intent['tag'] == predicted_class:
            responses = intent['responses']
            res = random.choice(responses)
            return res
