# db/firestore.py
import os
from firebase_admin import credentials, firestore, storage, initialize_app

def initialize_firebase():
    service_account_key_path = os.path.join(os.path.dirname(__file__), "../Keys", "nircars-firebase-adminsdk-eqsak-5cf240d333.json")
    
    if not os.path.exists(service_account_key_path):
        raise FileNotFoundError(f"Service account key file not found: {service_account_key_path}")

    cred = credentials.Certificate(service_account_key_path)
    app = initialize_app(cred, {'storageBucket': 'nircars.appspot.com'})

    db = firestore.client(app)
    bucket = storage.bucket()
    return db, bucket
