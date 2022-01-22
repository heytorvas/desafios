from telegram.ext import Updater, CommandHandler
from scraping import get_threads
import logging, os

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
logging.basicConfig(filename="bot.log", level=logging.INFO)

def threads(update, context):
    """Send a message when the command /NadaPraFazer is issued."""
    try:
        logging.info(f'command /NadaPraFazer {context.args[0]}')
        lists = get_threads(context.args[0])
        for threads in lists:
            for t in threads:
                try:
                    subreddit = t.__dict__['subreddit']
                    title = t.__dict__['title']
                    score = t.__dict__['score']
                    link = t.__dict__['link']
                    comments = t.__dict__['comments']
                    datetime = t.__dict__['datetime']
                    update.effective_message.reply_html(
                        f'<b>Subreddit: </b>{subreddit}\n'
                        f'<b>Title: </b>{title}\n'
                        f'<b>Score: </b>{score}\n'
                        f'<b>Link: </b>{link}\n'
                        f'<b>Comments: </b>{comments}\n'
                        f'<b>Datetime: </b>{datetime}\n'
                    )
                except:
                    subreddit = threads['subreddit']
                    msg = threads['msg']
                    update.effective_message.reply_html(
                        f'<b>Subreddit: </b>{subreddit}\n'
                        f'<b>Msg: </b>{msg}\n'
                    )
                    break
    except:
        logging.info('command /NadaPraFazer without arguments')
        update.message.reply_text('WRONG! Example: /NadaPraFazer askreddit;worldnews;cats')

def main():
    """Start the bot."""
    logging.info('bot on')
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(ACCESS_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("NadaPraFazer", threads, pass_args=True))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

main()