# Odoo Messenger Bot
This is a Telegram bot built using the python-telegram-bot library, designed to interact with users and provide responses. It is intended for integration with the Odoo system and responds to different user commands and messages.

## Features
- Start Command: Greets the user when the bot is started.
- Help Command: Provides a list of available commands and how to use them.
- Custom Command: Placeholder for any custom commands.
- Message Handling: Responds to user messages with predefined responses (e.g., "Hello", "How are you?, I love Python").

## Installation
1. Clone the repository to your local machine:
```bash
git clone https://github.com/pablo727/odoo_messenger_bot.git
cd odoo_messenger_bot
```
2. Create a virtual environment:
```bash
python -m venv odoo-venv
```
3. Activate the virtual environment:
   - On Windows:
   ```bash
   odoo-venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source odoo-venv/bin/activate
   ```
4. Add your Telegram bot token and bot username to the script or environment variables.

## Usage
1. Start the bot by running the script:
```bash
python main.py
```
2. The bot will respond to the following commands:
/start: Greets the user.
/help: Provides a list of available commands.
/custom: Executes a custom command (for testing or custom actions).
Other responses can be triggered by typing a message such as "hello", "how are you", or "I love python".
3. The bot can also handle group messages and respond when tagged with the bot's username.

## Configuration
- The bot uses the python-telegram-bot library.
- Make sure to update the TOKEN and BOT_USERNAME variables with your bot's token and username from BotFather.

## Contributing
If you'd like to contribute to this project, feel free to open a pull request or report any issues you find. Contributions are welcome!
1. Fork the repository.
2. Create your feature branch (git checkout -b feature-name).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-name).
5. Open a pull request.

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).







