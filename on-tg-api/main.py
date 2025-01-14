import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я ваш бот.')

async def main() -> None:
    app = ApplicationBuilder().token("6493157409:AAElg1VuCGMYuEoaQTJOTlqheiDyWXrtcSw").build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
