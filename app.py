from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from chatbot import Chatbot
import json
import pickle
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

chatbot = Chatbot()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_message = db.Column(db.Text, nullable=False)
    bot_response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))

def create_tables():
    with app.app_context():
        db.create_all()
        
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(username='admin', email='admin@college.edu', password=generate_password_hash('admin123'), is_admin=True)
            db.session.add(admin)
            db.session.commit()

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['is_admin'] = user.is_admin
            return redirect(url_for('index'))
        
        return render_template('login.html', error='Invalid email or password')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(email=email).first():
            return render_template('signup.html', error='Email already exists')
        
        if User.query.filter_by(username=username).first():
            return render_template('signup.html', error='Username already taken')
        
        user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect(url_for('login'))

@app.route('/chat', methods=['POST'])
def chat():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    user_message = request.json['message']
    bot_response = chatbot.get_response(user_message)
    
    chat_history = ChatHistory(user_id=session['user_id'], user_message=user_message, bot_response=bot_response)
    db.session.add(chat_history)
    db.session.commit()
    
    return jsonify({'response': bot_response})

@app.route('/admin')
def admin():
    if 'user_id' not in session or not session.get('is_admin'):
        return redirect(url_for('login'))
    
    users = User.query.all()
    faqs = FAQ.query.all()
    chat_history = ChatHistory.query.all()
    
    return render_template('admin.html', users=users, faqs=faqs, chat_history=chat_history)

@app.route('/admin/faq/add', methods=['POST'])
def add_faq():
    if 'user_id' not in session or not session.get('is_admin'):
        return jsonify({'error': 'Not authorized'}), 403
    
    question = request.form['question']
    answer = request.form['answer']
    category = request.form['category']
    
    faq = FAQ(question=question, answer=answer, category=category)
    db.session.add(faq)
    db.session.commit()
    
    return redirect(url_for('admin'))

@app.route('/admin/faq/delete/<int:faq_id>')
def delete_faq(faq_id):
    if 'user_id' not in session or not session.get('is_admin'):
        return redirect(url_for('login'))
    
    faq = FAQ.query.get_or_404(faq_id)
    db.session.delete(faq)
    db.session.commit()
    
    return redirect(url_for('admin'))

@app.route('/admin/train', methods=['POST'])
def train_model():
    if 'user_id' not in session or not session.get('is_admin'):
        return jsonify({'error': 'Not authorized'}), 403
    
    import subprocess
    subprocess.call(['python', 'train_model.py'])
    
    return redirect(url_for('admin'))

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=5000)
