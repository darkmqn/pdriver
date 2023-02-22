from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from googlesearch import search

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('Welcome to Printer Driver Bot! Please enter the model of your printer.')

# Define a function to handle user messages
def handle_message(update, context):
    model = update.message.text
    query = f'{model}hp printer driver download'
    for url in search(query, num_results=5):
        if 'download' in url:
            update.message.reply_text(f'Here is the link to download the driver for {model}: {url}')
            return
    update.message.reply_text(f'Sorry, I could not find a download link for the driver of {model}.')

# Create an updater and pass in your bot's API token
updater = Updater('5988660271:AAHO2orPTjadufPH8ek626d5ZjnErN7RBmw', use_context=True)

# Add handlers for the /start command and user messages
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

# Start the bot
updater.start_polling()
updater.idle()
