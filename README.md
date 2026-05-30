# College FAQ AI Chatbot

## Project Overview
An intelligent AI-powered chatbot system that automatically answers college-related frequently asked questions using Machine Learning and Natural Language Processing.

## Tech Stack
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, NLTK
- **Database**: SQLite (SQLAlchemy ORM)

## Features
1. **Authentication Module**: Student login/signup, Admin login, Session management, Password hashing
2. **Chatbot Features**: Real-time chat interface, Intent recognition, Smart automated responses, Chat history
3. **NLP Pipeline**: Text preprocessing, TF-IDF Vectorization, Intent classification
4. **Machine Learning**: Trained on FAQ dataset, Multiple algorithms (Logistic Regression, Naive Bayes, SVM)
5. **Admin Dashboard**: Add/edit/delete FAQs, Train model button, View chatbot analytics
6. **Quick Suggestions**: Auto-suggestion buttons for common questions

## Installation

### Step 1: Clone or Download the Project

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
- **Windows**:
```bash
venv\Scripts\activate
```
- **Mac/Linux**:
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Train the Machine Learning Model
```bash
python train_model.py
```

### Step 6: Run the Application
```bash
python app.py
```

## Usage

### Access the Application
Open your browser and go to: `http://localhost:5000`

### Default Admin Credentials
- Email: `admin@college.edu`
- Password: `admin123`

### Student
1. Sign up for an account
2. Login with your credentials
3. Start chatting with the AI assistant

### Admin
1. Login with admin credentials
2. Access Admin Dashboard
3. Add/Delete FAQs
4. Train the model
5. View chat history

## Project Structure
```
chatbot/
├── app.py
├── train_model.py
├── chatbot.py
├── requirements.txt
├── README.md
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── index.html
│   └── admin.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── chat.js
├── datasets/
│   ├── intents.json
│   └── faq_dataset.csv
├── trained_models/
│   ├── chatbot_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── intents_data.pkl
└── chatbot.db (generated after first run)
```

## Deployment Options

### Localhost
Follow installation instructions above.

### PythonAnywhere
1. Upload project files to PythonAnywhere
2. Create virtual environment and install dependencies
3. Train model
4. Configure WSGI file
5. Reload application

### Render
1. Push project to GitHub
2. Connect repository to Render
3. Configure environment variables
4. Deploy

### Railway
1. Push project to GitHub
2. Connect repository to Railway
3. Deploy

## Dataset
The dataset contains FAQs about:
- Admissions
- Courses
- Fees
- Hostel
- Placements
- Scholarships
- Transport
- Exams
- Timetable
- Faculty
- Library
- Campus

## Future Enhancements
- Voice input and text-to-speech
- Multi-language support
- Dark/light mode
- FAQ recommendation system
- Sentiment analysis

## License
MIT License
