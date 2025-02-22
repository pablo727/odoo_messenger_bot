from typing import Final
from telegram import Update
from telegram.ext import(
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(filename='bot_errors.log', level=logging.ERROR)

# Load environment variables from the .env file
load_dotenv()

# Get the Telegram bot token from the environment variable
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Make sure the token is loaded correctly
if TOKEN is None:
    logging.error("Error: TELEGRAM_TOKEN is not set!")
else:
    logging.info("Token loaded successfully!")

BOT_USERNAME: Final = '@OdooMessengerBot'


# Global error handler
async def global_error_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors globaly for the bot."""
    try:
        # Log the error
        logging.error(f"An error ocurred: {context.error}")
        # Optionally, you can send a message to the admin or log it to a file
        await update.message.reply_text(
            'Oops! Something went wrong. Please try again later.')
    except Exception as e:
        # In case the error handler itself throws an error, log it
        logging.error(f"Error in the global error handler: {e}")



# Commands
try:
    async def start_command(
        update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            await update.message.reply_text(
                'Hello! Thanks for chatting with me!')
        except ValueError:
            # Handle or log the ValueError if needed, and continue
            logging.error("ValueError ocurred in the start_command")
            pass  # Continue without interrupting the flow

    async def help_command(
        update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            await update.message.reply_text(
                'I am Odoo bot! Please type something so I can respond!')
        except ValueError:
            # Handle or log the ValueError if needed, and continue
            logging.error("ValueError ocurred in the help_command")
            pass  # Continue without interrupting the flow

    async def custom_command(
        update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            await update.message.reply_text('This is a custom command!')
        except ValueError:
            logging.error("ValueError ocurred in the custom_command")
            pass  # Continue without interrupting the flow

except Exception as e:
    logging.error(f"An unexpected error ocurred: {e}")


# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how are you' in processed:
        return 'I am good!'
    
    if 'i love python' in processed:
        return 'Awesome! Python is great! What do you want to learn next?'
    
    return 'I do not understand what you wrote...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    # Log the user's message
    logging.info(
        f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    # Log the bot's response
    logging.info(f"Bot:, {response}")
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f"Update {update} cause error {context.error}")


if __name__ == '__main__':
    logging.info('Startin bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    logging.info('Polling...')
    app.run_polling(poll_interval=3)
