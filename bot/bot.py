import os

import aiogram
import structlog

logger = structlog.get_logger('bot')

def run():
    bot = aiogram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    dp = aiogram.Dispatcher(bot)

    @dp.message_handler(commands=['hello'])
    async def hello_handler(message: aiogram.types.Message):
         await message.reply(f'Hello, {message.from_user.full_name}')

    @dp.message_handler(content_types=[aiogram.types.ContentType.PHOTO])
    async def handle(message: aiogram.types.Message):
        logger.info(message)
        if message.caption.lower() == 'славик':
            await message.delete()
    
    aiogram.executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    run()