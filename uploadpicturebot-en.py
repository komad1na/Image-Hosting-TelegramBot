import requests
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext
)

CHOOSING, TYPING_CHOICE = range(2)

reply_keyboard = [
    ['/Upload_picture'],
]

# Markup keyboard after starting command
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def start(update: Update, context: CallbackContext) -> int:
    """Welcoming user."""
    update.message.reply_text(
        "Welcome dear guests. Press /Upload_picture for beginning.",
        reply_markup=markup,
    )
    return CHOOSING


def regular_choice(update: Update, context: CallbackContext):
    # Bot takes photo you sent in chat to upload it
    filephoto = context.bot.get_file(update.message.photo[-1].file_id)
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": "AUTH KEY FROM IMGBB ", # here you should add your api key for imgbb
        "image": filephoto.file_path
    }
    res = requests.post(url, payload)
    if(res.status_code == 200):
        response = 'Picture is successfully uploaded. \n\nLink:\n'

        # Extracting the link from server response
        ceocontent = res.text.split(',')
        link = ceocontent[2].split('"')
        linkovi = link[3].replace("\\",'')

    else:
        response = 'There has been an error proccessing your request.'
        linkovi = "N/A"

    # Bot sends message with response including link
    context.bot.send_message(chat_id=update.message.chat_id, text=response+linkovi,disable_web_page_preview=True)

    # Bot automatically deletes picture from chat
    context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)

    # Bot deletes the message saying "Send me a photo for upload' for cleaner
    context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id - 1)

    # Bot pins the messages with link in them and you can access it in pinned messages for all links
    context.bot.pinChatMessage(chat_id=update.message.chat_id, message_id=update.message.message_id + 1, disable_notification=True)

    # Bot deletes notification about pinning last message
    context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id + 2)

    return CHOOSING


def custom_choice(update: Update, context: CallbackContext) -> int:
    """Ask the user for a photo."""
    update.message.reply_text(
        'Send me a photo for upload'
    )

    return TYPING_CHOICE


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("BOTS TOKEN GOES HERE")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING and TYPING_CHOICE
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING:
            [
                MessageHandler(Filters.regex('^(/Upload_picture)$'), custom_choice)
            ],
            TYPING_CHOICE:
            [
                MessageHandler(Filters.photo, regular_choice)
            ],
        },
        fallbacks=[],
    )

    # Add handler into dispatcher
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
