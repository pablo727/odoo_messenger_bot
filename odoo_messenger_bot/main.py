import xmlrpc.client
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Odoo credentials from the .env file
ODOO_URL = os.getenv("ODOO_URL")
DB_NAME = os.getenv("DB_NAME")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

# Telegram bot token from .env
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Log setup
logging.basicConfig(filename='bot_errors.log', level=logging.ERROR)

# Connect to Odoo
common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
uid = common.authenticate(DB_NAME, USER_NAME, PASSWORD, {})
models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')

# Check if the token is loaded correctly
if TOKEN is None:
    logging.error("Error: TELEGRAM_TOKEN is not set!")
else:
    logging.info("Token loaded successfully!")

# Telegram Bot Handler Functions
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your Odoo Messenger Bot.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'I can help you interact with Odoo.'
        'Try sending commands like /get_partners.')

async def get_partners(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Fetch partners (customers) from Odoo and send them as a message"""
    try:
        partners = models.execute_kw(
            DB_NAME, uid, PASSWORD, 'res.partner', 'search_read',
            [[]], {'fields': ['name', 'email']}
        )
        response = "Here are the partners:\n"
        for partner in partners:
            response += f"Name: {partner['name']}, Email: {partner.get(
                'email', 'No Email')}\n"
        await update.message.reply_text(response)
    except Exception as e:
        logging.error(f"Error fetching partners: {e}")
        await update.message.reply_text(
            "Sorry, I couldn't fetch the partners from Odoo."
            )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()
    if 'hello' in message:
        await update.message.reply_text(
            'Hey there! How can I assist you with Odoo today?'
            )
    elif 'help' in message:
        await help_command(update, context)
    elif 'partners' in message:
        await get_partners(update, context)
    else:
        await update.message.reply_text("Sorry, I didn't understand that.")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Command Handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('get_partners', get_partners)) 

    # Message Handler
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message)
        )

    # Error Handler
    app.add_error_handler(error)

    # Polling to keep the bot running
    logging.info('Polling for messages...')
    app.run_polling(poll_interval=3)

