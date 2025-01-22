# python-telegram-bot library required!
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final[str] = 'bot_token'
BOT_USERNAME: Final[str] = '@bot_tg_tag'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Здарова нафег!!')

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'пр' in processed:
        return 'ивет'
    return 'ok'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Лог
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # Тип ввода сообщения
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    # Ответ
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Обнова {update} с ошибкой: {context.error}')

def main():
    print('Старт ботяры')
    app = Application.builder().token(TOKEN).build()

    # Команды
    app.add_handler(CommandHandler('start', start_command))

    # Сообщения
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Ошибки
    app.add_error_handler(error)

    print('Поллинг...')
    app.run_polling(poll_interval=5)

if __name__ == '__main__':
    main()
