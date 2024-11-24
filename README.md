                                                        Personal AI Chatbot

A modular and interactive Python-based AI chatbot that combines conversational capabilities with practical features like opening websites, launching apps, and handling user authentication. This project leverages NLP for enhanced command processing and supports easy customization for additional functionality.

😊Features
🗣️ Conversational Capabilities
Predefined responses to over 50+ questions stored in a JSON file.
Uses NLP for flexible matching, allowing partial and case-insensitive input.
Sample questions:
"How are you?"
"Who created you?"
"What is the meaning of life?"

🌐 Website Commands
Opens popular websites using natural language commands.
Examples:
open youtube
launch wikipedia

📱 App Commands
Launches system-installed apps directly from the chatbot.
Examples:
start spotify
run telegram

🔒 User Authentication
Secures user sessions with a username and password.
New users can register, while existing users can log in.
Passwords are hashed for secure storage in user_data.json.

🛠️ Customization
Add or edit conversational responses by updating conversation.json.
Extend supported apps and websites by modifying app_opener.py and web_opener.py.

Installation
Prerequisites
Python 3.8+ installed on your system.
A virtual environment (optional but recommended).

Steps
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/personal-ai-chatbot.git
cd personal-ai-chatbot
Set Up a Virtual Environment (optional):

bash
Copy code
python -m venv env
source env/bin/activate    # On macOS/Linux
env\Scripts\activate       # On Windows
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Chatbot:

bash
Copy code
python main.py
File Structure
bash
Copy code
personal-ai-chatbot/
├── main.py               # Entry point for the chatbot
├── chatbot_logic.py      # Handles conversation and command processing
├── database.py           # Manages user authentication
├── web_opener.py         # Opens websites
├── app_opener.py         # Launches system apps
├── conversation.json     # Stores conversational questions and answers
├── user_data.json        # Stores user credentials securely
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
Usage
Starting the Chatbot
Run main.py.
Log in or register as a new user.
Enter commands or chat naturally with the bot.
Examples
Conversation:

Input: how are you
Output: I'm just a bot, but I'm doing great! How can I assist you?
Open Websites:

Input: launch youtube
Output: Opening YouTube...
Launch Apps:

Input: start spotify
Output: Opening Spotify...
Customization
Add New Conversational Responses
Open conversation.json.
Add a new key-value pair under "questions_and_answers". Example:
json
Copy code
{
    "questions_and_answers": {
        "what is your favorite color": "I like all colors equally!"
    }
}
Add New Supported Websites
Open web_opener.py.
Add a new entry to the WEBSITES dictionary. Example:
python
Copy code
WEBSITES = {
    "youtube": "https://www.youtube.com",
    "quora": "https://www.quora.com"  # New entry
}
Add New Supported Apps
Open app_opener.py.
Add a new entry to the APPS dictionary. Example:
python
Copy code
APPS = {
    "spotify": "spotify",
    "slack": "slack"  # New entry
}
Dependencies
nltk: For natural language processing.
webbrowser: For opening websites.
os: For launching system applications.
json: For handling conversational data and user authentication.
Install all dependencies with:

bash
Copy code
pip install -r requirements.txt
Contributing
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have questions or need support, feel free to reach out:

Email: harshbabhre2404@gmail.com.com
GitHub: Your GitHub Profile







