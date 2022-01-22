from telegram.ext import Updater, CommandHandler
from scraping import get_threads
import logging, os

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
logging.basicConfig(filename="bot.log", level=logging.INFO)

def threads(update, context):
    """
    Send a message when the command /NadaPraFazer is issued.
    """
    try:
        logging.info(f'command /NadaPraFazer {context.args[0]}')
        lists = get_threads(context.args[0])
        for threads in lists:
            for reddit in threads:
                try:
                    subreddit = reddit.__dict__['subreddit']
                    title = reddit.__dict__['title']
                    score = reddit.__dict__['score']
                    link = reddit.__dict__['link']
                    comments = reddit.__dict__['comments']
                    datetime = reddit.__dict__['datetime']
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
    """
    Start the bot.
    """
    logging.info('bot on')

    updater = Updater(ACCESS_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("NadaPraFazer", threads, pass_args=True))

    updater.start_polling()
    updater.idle()

main()