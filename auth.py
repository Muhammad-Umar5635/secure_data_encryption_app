import base64
import hashlib
import os
import time
from utils import is_locked_out

def hash_passkey_pbkdf2(passkey, salt=None):
    if salt is None:
        salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', passkey.encode(), salt, 100000)
    return base64.b64encode(salt).decode(), base64.b64encode(hashed).decode()

def verify_passkey_pbkdf2(passkey, stored_salt, stored_hash):
    salt = base64.b64decode(stored_salt)
    new_hash = hashlib.pbkdf2_hmac('sha256', passkey.encode(), salt, 100000)
    return base64.b64encode(new_hash).decode() == stored_hash

def register_user(username, passkey, users):
    if username in users:
        return False
    salt, hashed_passkey = hash_passkey_pbkdf2(passkey)
    users[username] = {
        "salt": salt,
        "hashed_passkey": hashed_passkey,
        "data": "",
        "failed_attempts": 0
    }
    return True

def authenticate_user(username, passkey, users):
    if username not in users:
        return False, "User does not exist."
    user = users[username]
    locked, wait_time = is_locked_out(user)
    if locked:
        return False, f"Too many failed attempts. Try again in {wait_time} seconds."
    if verify_passkey_pbkdf2(passkey, user["salt"], user["hashed_passkey"]):
        user["failed_attempts"] = 0
        return True, "Authenticated"
    else:
        user["failed_attempts"] += 1
        if user["failed_attempts"] >= 3:
            user["lockout_time"] = time.time()
        return False, "Incorrect passkey."

def get_user_data(users, username):
    return users[username]