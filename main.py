import logging
import requests
from config import TG_TOKEN
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update, context):
    user = update.effective_user
    logger.info('%s стартанул бота', user.first_name)
    await update.message.reply_text(
        f"Здравствуйте, {user.first_name}. Это бот со случайными мемами.\n",
        reply_markup=ReplyKeyboardMarkup([['Покажи мемчик!']], resize_keyboard=True)
    )


async def meme(update, context):
    response = requests.get('https://meme-api.com/gimme').json()
    await update.message.reply_photo(response['url'],
                                     reply_markup=ReplyKeyboardMarkup([['Еще мемчик!']], resize_keyboard=True))
    logger.info('%s смотрит мем %s', update.effective_user.first_name, response['url'])


def main():
    application = Application.builder().token(TG_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, meme))
    application.add_handler(CommandHandler("meme", meme))
    application.run_polling()


if __name__ == "__main__":
    main()
