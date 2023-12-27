import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler, filters, MessageHandler
from knn import search_similar_medicines_short

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '6771383484:AAGNXrH62Qrj0DkElnDmQKsAZMdTubIZ_l0'

# Определение состояний для конечного автомата
ENTER_MEDICINE = 0


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='''I'm a MedSim bot! I could help you to find analogues of your medicine. \nJust type the name of your medicine in English or Russian.\n\nПривет, я бот проекта MedSim. Я помогу тебе найти похожие лекарства на основании их текстовых описаний.\nПросто введи название лекарства, для которого ты хочешь найти аналоги'''
    )

async def enter_medicine(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Please enter the name of the medicine:'
    )
    return ENTER_MEDICINE

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def findsim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    medicine_name = update.message.text
    try:
        text_caps = search_similar_medicines_short(medicine_name)
    except:
        text_caps = "Unfortunately, I don't have this medicine in my database. Or maybe there is a mistake in the name :)\n К сожалению, я не могу выполнить запрос. Это случается, если введенного названия нет в моей базе данных, или в случае ошибки в написании названия"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    findsim_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), findsim)


    application.add_handler(start_handler)
    application.add_handler(findsim_handler)


    application.run_polling()


if __name__ == '__main__':
    main()
