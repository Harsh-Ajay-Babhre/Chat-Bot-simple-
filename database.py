import json
import os
import hashlib

USER_DATA_FILE = "user_data.json"

def setup_user_data_file():
    """
    Ensure the user data JSON file exists and is properly initialized.
    """
    if not os.path.exists(USER_DATA_FILE) or os.stat(USER_DATA_FILE).st_size == 0:
        with open(USER_DATA_FILE, "w") as file:
            json.dump({"users": {}}, file)

def hash_password(password):
    """
    Hash the password using SHA-256 for secure storage.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(username, password):
    """
    Authenticate an existing user by checking their username and hashed password.
    """
    with open(USER_DATA_FILE, "r") as file:
        data = json.load(file)

    if username in data["users"]:
        stored_password_hash = data["users"][username]
        if hash_password(password) == stored_password_hash:
            return True  # Authentication successful
        else:
            print("Incorrect password. Please try again.")
            return False
    else:
        print("Username not found.")
        return False

def register_user():
    """
    Register a new user by taking a username and password.
    """
    setup_user_data_file()

    with open(USER_DATA_FILE, "r") as file:
        data = json.load(file)

    username = input("Enter a new username: ").strip()
    if username in data["users"]:
        print("This username is already taken. Please try again.")
        return None

    password = input("Enter a new password: ").strip()
    password_hash = hash_password(password)

    data["users"][username] = password_hash

    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Welcome, {username}! Your registration is successful.")
    return username

def start_session():
    """
    Handle user login or registration.
    """
    print("Welcome to the Chatbot!")
    setup_user_data_file()

    while True:
        choice = input("Are you a registered user? (yes/no): ").strip().lower()

        if choice == "yes":
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            if authenticate_user(username, password):
                print(f"Hello, {username}! Authentication successful. Let's start your session.")
                return username

        elif choice == "no":
            username = register_user()
            if username:
                print(f"Hello, {username}! Let's start your session.")
                return username

        else:
            print("Invalid input. Please type 'yes' or 'no'.")
