import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("firebase_key.json")
if firebase_admin.initialize_app(cred):
    print("Firebase was Initialized")
