from time import sleep
from picamera import PiCamera
import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


BOT_TOKEN = '732652076:AAFqNOuSq_Xx50NKWpK9XfV7bUOzrydxFC4'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def takepic():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview(alpha=200)
    # Camera warm-up time
    sleep(2)
    image=camera.capture('./whiteboard.jpg')
    camera.close()
    return image

def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def sendpicture(bot, update):
    print('USER ASKED TO SEND PICTURE')
    chat_id = update.message.chat_id

    '''TAKE THE PHOTO HERE, STORE IT IN A VARIABLE, THEN EITHER SEND THE FIREBASELINK OR THE FILE BELOW WITH photo=image, WHERE image=open(filename, rb)'''
    
    image=takepic()
    image = open('./whiteboard.jpg', 'rb')
    bot.send_photo(chat_id=chat_id, photo=image)

def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("takepicture", sendpicture))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()