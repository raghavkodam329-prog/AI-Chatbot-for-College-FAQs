
print("Testing imports...")
try:
    from flask import Flask
    print("✅ Flask imported successfully!")
except Exception as e:
    print(f"❌ Flask import error: {e}")

try:
    from flask_sqlalchemy import SQLAlchemy
    print("✅ Flask-SQLAlchemy imported successfully!")
except Exception as e:
    print(f"❌ Flask-SQLAlchemy import error: {e}")

try:
    from werkzeug.security import generate_password_hash, check_password_hash
    print("✅ Werkzeug imported successfully!")
except Exception as e:
    print(f"❌ Werkzeug import error: {e}")

try:
    import pickle
    print("✅ Pickle imported successfully!")
except Exception as e:
    print(f"❌ Pickle import error: {e}")

try:
    # Check if trained models exist
    import os
    if os.path.exists("trained_models/chatbot_model.pkl") and os.path.exists("trained_models/tfidf_vectorizer.pkl") and os.path.exists("trained_models/intents_data.pkl"):
        print("✅ All trained models exist!")
    else:
        print("❌ Some trained models are missing!")
except Exception as e:
    print(f"❌ Error checking models: {e}")

print("\nAll tests completed!")
