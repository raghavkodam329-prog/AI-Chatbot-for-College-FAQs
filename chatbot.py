import pickle
import random
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

class Chatbot:
    def __init__(self):
        self.model = pickle.load(open('trained_models/chatbot_model.pkl', 'rb'))
        self.tfidf = pickle.load(open('trained_models/tfidf_vectorizer.pkl', 'rb'))
        self.intents_data = pickle.load(open('trained_models/intents_data.pkl', 'rb'))
    
    def preprocess_text(self, text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = nltk.word_tokenize(text)
        tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
        return ' '.join(tokens)
    
    def get_response(self, user_input):
        processed_input = self.preprocess_text(user_input)
        input_tfidf = self.tfidf.transform([processed_input])
        tag = self.model.predict(input_tfidf)[0]
        
        for intent in self.intents_data['intents']:
            if intent['tag'] == tag:
                return random.choice(intent['responses'])
        
        return "I'm sorry, I don't understand that. Can you please rephrase your question?"
