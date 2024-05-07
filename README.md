This Python script sets up a Telegram chat bot using the Telegram Bot API. It responds to user messages, provides news headlines from Hindustan Times, and fetches images from iStockPhoto based on user input. Additionally, it handles various commands and error scenarios.

Requirements
Python 3.x
python-telegram-bot library
beautifulsoup4 library
requests library
Usage
Replace 'YOUR_TOKEN' in the Token variable with your actual Telegram Bot API token.
Ensure the dependencies are installed (python-telegram-bot, beautifulsoup4, requests).
Create two JSON files: intents.json and intentes1.json, and populate them with the provided data or customize as needed.
Run the bot.py script.
Interact with the bot in a Telegram chat.
Features
Greetings, Thanks, Goodbye: Responds to common greetings, expressions of gratitude, and farewells.
Command Handling: Responds to specific commands like /start, /image, and /news.
News Headlines: Retrieves headlines from Hindustan Times based on user-selected categories.
Image Retrieval: Fetches images from iStockPhoto based on user-specified categories.
Error Handling: Handles errors gracefully, logging them for further analysis.
Customization
Token: Replace 'YOUR_TOKEN' with your actual Telegram Bot API token.
JSON Data: Customize the intents and categories in the JSON files to tailor responses and functionality to your needs.
Additional Features: Extend the bot's capabilities by adding more command handlers and response logic
