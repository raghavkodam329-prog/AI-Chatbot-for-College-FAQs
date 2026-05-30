import json
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return ' '.join(tokens)

def load_data():
    with open('datasets/intents.json', 'r') as f:
        data = json.load(f)
    
    questions = []
    tags = []
    
    for intent in data['intents']:
        for pattern in intent['patterns']:
            questions.append(pattern)
            tags.append(intent['tag'])
    
    return questions, tags, data

def train_models():
    questions, tags, intents_data = load_data()
    
    processed_questions = [preprocess_text(q) for q in questions]
    
    X_train, X_test, y_train, y_test = train_test_split(processed_questions, tags, test_size=0.2, random_state=42)
    
    tfidf = TfidfVectorizer(max_features=1000)
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)
    
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Multinomial Naive Bayes': MultinomialNB(),
        'SVM': SVC(kernel='linear', probability=True)
    }
    
    best_model = None
    best_accuracy = 0
    results = {}
    
    for name, model in models.items():
        model.fit(X_train_tfidf, y_train)
        y_pred = model.predict(X_test_tfidf)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy
        print(f"\n{name} Accuracy: {accuracy:.4f}")
        print(classification_report(y_test, y_pred, zero_division=0))
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model
    
    print(f"\nBest Model: {[name for name, acc in results.items() if acc == best_accuracy][0]} with accuracy: {best_accuracy:.4f}")
    
    pickle.dump(best_model, open('trained_models/chatbot_model.pkl', 'wb'))
    pickle.dump(tfidf, open('trained_models/tfidf_vectorizer.pkl', 'wb'))
    pickle.dump(intents_data, open('trained_models/intents_data.pkl', 'wb'))
    
    print("\nModels saved successfully!")

if __name__ == "__main__":
    train_models()
