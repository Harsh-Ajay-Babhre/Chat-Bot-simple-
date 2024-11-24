from database import start_session
from chatbot_logic import handle_command, handle_chat
import time

def greet_user():
    """
    Generate a dynamic greeting message based on the time of day.
    """
    current_hour = time.localtime().tm_hour
    if 5 <= current_hour < 12:
        return "Good Morning!"
    elif 12 <= current_hour < 17:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

def display_menu():
    """
    Display the main menu for the chatbot's functionalities.
    """
    print("\nWhat would you like to do?")
    print("1. Chat")
    print("2. Commands (Open websites/apps)")
    print("3. Exit")

def main():
    """
    Main entry point for the chatbot.
    """
    print("Welcome to your Personal Chatbot!")
    # Register user and start session
    username = start_session()

    # Personalized greeting after registration
    print(f"{greet_user()}, {username}! How can I assist you today?")

    # Main menu loop
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            # Chat functionality
            while True:
                user_input = input("Chat with me (type 'back' to return to menu): ").strip()
                if user_input.lower() == "back":
                    break
                handle_chat(user_input)

        elif choice == "2":
            # Command functionality
            while True:
                user_input = input("Enter your command (type 'back' to return to menu): ").strip()
                if user_input.lower() == "back":
                    break
                handle_command(username, user_input)

        elif choice == "3" or exit:
            print(f"Goodbye, {username}! Have a great day!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
