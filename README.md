# Odoo Messenger Bot
This project provides a simple Telegram bot that interacts with your Odoo instance to fetch customer (partner) information using the Odoo XML-RPC API.

<p align="center">
  <img src="image/odoo_bot.webp" alt="Odoo Messenger Bot" width="300" height="300"/>
</p>

## Features
- **/start**: Greets the user and starts the bot.
- **/help**: Provides information on how to use the bot.
- **/get_partners**: Fetches and displays a list of customer names and emails from your Odoo database.

## Requirements
- Python 3.13+
- Create a Bot on Telegram using BotFather and obtain the Bot Token.
- Odoo account and database (fake or real).
- `.env` file to store sensitive information.

## Setup
### 1. Clone the repository to your local machine:
```bash
git clone https://github.com/pablo727/odoo_messenger_bot.git
cd odoo_messenger_bot
```

### 2. Create a virtual environment:
It’s recommended to create a virtual environment to keep dependencies isolated:
```bash
python -m venv odoo-venv
```
  Activate the virtual environment:
   - On Windows:
   ```bash
   odoo-venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source odoo-venv/bin/activate
   ```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Set Up the .env File
Create a .env file in the root of the project with the following information:
```ini
# Odoo credentials (replace with your actual Odoo details)
ODOO_URL=http://your-odoo-instance-url.com
DB_NAME=your-odoo-database-name
USER_NAME=your-odoo-username
PASSWORD=your-odoo-password

# Telegram bot token (replace with your actual bot token)
TELEGRAM_TOKEN=your-telegram-bot-token
```
Make sure not to upload your .env file to public repositories for security reasons.

### 5. Set Up Odoo
1. Create an Odoo Account: Create a free Odoo account at Odoo.
2. Create a Database: If you're using a test account, create a database for testing and leave it empty, 3. or populate it with sample data.
4. Add Partners: You can add customer information under the Contacts section in Odoo to test the bot.

### 6. Running the Bot
Run the bot with the following command:
```bash
python main.py
```
Once the bot is running, open Telegram and search for your bot using its username, then try using the commands /start, /help, and /get_partners.

### 7. Commands
- /start: Starts the bot and sends a greeting message.
- /help: Displays a list of commands and how to use the bot.
- /get_partners: Fetches customer information (partners) from your Odoo database and sends it to the user.

### Example Output
When you run the /get_partners command, the bot will reply with a list of customers in your Odoo database. Example:
```yaml
Here are the partners:
Name: John Doe, Email: john.doe@email.com
```

### 8. Error Handling
If there are any issues fetching partners from Odoo, the bot will log the error in the bot_errors.log file, and users will receive a message saying:
```vbnet
Sorry, I couldn't fetch the partners from Odoo.
```

### Troubleshooting
- Bot is not responding: Make sure you have a stable internet connection and that the Telegram bot token and Odoo credentials are correct.
- No partners fetched: Check if the Odoo database has customer records (partners) in the Contacts section. If not, add some for testing.

## Contributing
If you'd like to contribute to this project, feel free to open a pull request or report any issues you find. Contributions are welcome!
1. Fork the repository.
2. Create your feature branch (git checkout -b feature-name).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-name).
5. Open a pull request.

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
