# Project Documentation: AI Chatbot for College FAQs

## Abstract
This project presents an intelligent AI-powered chatbot system designed to automatically answer college-related frequently asked questions (FAQs). The system uses Natural Language Processing (NLP) and Machine Learning (ML) techniques to understand user queries and provide relevant responses. The chatbot features a user-friendly web interface, student authentication, admin dashboard, and intent classification using SVM, Logistic Regression, and Naive Bayes algorithms.

## Problem Statement
Colleges and universities receive thousands of queries from students and prospective students regarding admissions, courses, fees, placements, hostel facilities, and more. Answering these queries manually is time-consuming and resource-intensive. There is a need for an automated system that can provide instant, accurate responses to these FAQs 24/7.

## Objectives
1. To develop an AI-powered chatbot that can answer college-related FAQs
2. To implement NLP techniques for intent recognition and text preprocessing
3. To train and compare multiple ML algorithms for intent classification
4. To create a user-friendly web interface for students and admin
5. To implement authentication and session management
6. To build an admin dashboard for managing FAQs and chat history

## System Architecture
```
┌─────────────────┐
│   Web Client    │
│  (HTML/JS/CSS)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Flask Server  │
│   (Backend)     │
└────────┬────────┘
         │
         ├─────────────┬──────────────┐
         ▼             ▼              ▼
┌──────────────┐ ┌──────────┐ ┌───────────────┐
│  Chatbot     │ │ Database │ │  ML Models    │
│  (NLP)       │ │ (SQLite) │ │ (SVM/TF-IDF) │
└──────────────┘ └──────────┘ └───────────────┘
```

## Modules

### 1. Authentication Module
- User registration (Signup)
- User login
- Admin login
- Password hashing (Werkzeug security)
- Session management using Flask sessions

### 2. Chatbot Module
- Real-time chat interface
- Intent recognition using trained ML model
- Text preprocessing (tokenization, stopword removal, lemmatization)
- Response generation
- Chat history storage in database

### 3. NLP Pipeline
- Text preprocessing
- TF-IDF vectorization for feature extraction
- Intent classification using SVM (best performing model)

### 4. Machine Learning Module
- Dataset preparation
- Model training (Logistic Regression, Naive Bayes, SVM)
- Model evaluation
- Model persistence using Pickle

### 5. Admin Dashboard
- FAQ management (Add/Delete)
- Model training button
- Chat history view
- User statistics
- Analytics

## Dataset
The dataset is created in JSON format containing:
- 13 intent categories
- Multiple patterns per intent
- Multiple responses per intent

Categories: Greeting, Goodbye, Admissions, Courses, Fees, Hostel, Placements, Scholarships, Transport, Exams, Timetable, Faculty, Library, Campus

## Model Training and Evaluation

### Algorithms Compared
1. Logistic Regression - 61.11% accuracy
2. Multinomial Naive Bayes - 44.44% accuracy  
3. Support Vector Machine (SVM) - 66.67% accuracy

### Best Model
SVM (Support Vector Machine) with linear kernel was selected as the best model with 66.67% accuracy.

### Techniques Used
- Train-test split: 80-20
- Feature extraction: TF-IDF Vectorizer
- Evaluation metrics: Accuracy, Precision, Recall, F1-score

## Advantages
1. 24/7 availability
2. Instant responses
3. Reduces workload of college staff
4. Scalable and easy to maintain
5. User-friendly interface
6. Admin dashboard for easy management

## Future Scope
1. Voice input and text-to-speech functionality
2. Multi-language support
3. Dark/light mode toggle
4. Sentiment analysis of queries
5. FAQ recommendation system
6. Integration with college ERP system
7. Advanced deep learning models (LSTM, BERT)
8. Mobile application

## Viva Questions and Answers

### Q1. What is the purpose of this project?
A. The purpose of this project is to develop an AI-powered chatbot that can automatically answer college-related frequently asked questions, reducing the workload of college staff and providing instant responses to students.

### Q2. Which algorithms did you use and which one performed best?
A. We used Logistic Regression, Multinomial Naive Bayes, and SVM. SVM performed the best with 66.67% accuracy.

### Q3. What preprocessing techniques did you apply?
A. We applied text lowercasing, punctuation removal, tokenization, stopword removal, and lemmatization.

### Q4. What is TF-IDF?
A. TF-IDF (Term Frequency-Inverse Document Frequency) is a numerical statistic that reflects how important a word is to a document in a collection. It is used for feature extraction in text classification.

### Q5. What database did you use and why?
A. We used SQLite with SQLAlchemy ORM because it is lightweight, file-based, and easy to set up for small to medium applications.

### Q6. How is security handled in your application?
A. We use password hashing with Werkzeug security, session management, and separate admin and student roles.

### Q7. Can you explain the system architecture?
A. The system has a web frontend (HTML/JS/CSS), Flask backend server, NLP chatbot module, SQLite database, and trained ML models stored as pickle files.

### Q8. What are the future enhancements possible?
A. Future enhancements include voice input, multi-language support, sentiment analysis, deep learning models, mobile app, and ERP integration.

## Resume Content

### Project Title
AI Chatbot for College FAQs

### Project Description
Developed an intelligent AI-powered chatbot system using Flask, NLTK, and Scikit-learn that automatically answers college-related FAQs. The system features student authentication, real-time chat interface, admin dashboard for FAQ management, and intent classification using SVM algorithm with TF-IDF vectorization.

### Key Features
- Real-time chatbot with intent recognition
- Student and admin authentication with password hashing
- Admin dashboard for FAQ management and analytics
- Model training and comparison of 3 ML algorithms
- Chat history storage using SQLite
- Quick suggestion buttons for common queries

### Technical Skills Used
- Python, Flask
- Scikit-learn, NLTK
- HTML5, CSS3, JavaScript, Bootstrap 5
- SQLite, SQLAlchemy
- Natural Language Processing (NLP)
- Machine Learning (Classification)
- TF-IDF Vectorization
