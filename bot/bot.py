import os
import typing

import aiogram
import structlog

from bot.cartoonify import cartoonify

logger = structlog.get_logger('bot')

async def cartoonify_image(message: aiogram.types.Message, bot: aiogram.Bot):
    await message.answer('Got your image, result coming soon')
    original_file_id = message.photo[-1].file_id
    original_image = await bot.get_file(file_id=original_file_id)
    original_image_path = f'/tmp/bot_{original_file_id}.png'
    await original_image.download(destination_file=original_image_path, make_dirs=True)

    try:
        cartooned_image_path = cartoonify(original_image_path=original_image_path)
        with open(cartooned_image_path, 'rb') as cartooned_image:
            await message.answer_photo(photo=cartooned_image, caption='Here it is!')
    except Exception as e:
        logger.error(e)
        await message.answer('Something went wrong... I have already informed the developer. Try again later')
        cartooned_image_path = None
    finally:
        os.remove(original_image_path)
        if cartooned_image_path:
            os.remove(cartooned_image_path)
    return 

def run():
    bot = aiogram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    dp = aiogram.Dispatcher(bot)
    
    content_handlers: dict[str, typing.Callable] = {
        'cartoonify': cartoonify_image
    }

    @dp.message_handler(aiogram.filters.CommandStart())
    async def start_handler(message: aiogram.types.Message):
        return await message.answer('Send me pic with one of the listed captions:\n' + '\n'.join(content_handlers.keys()))

    @dp.message_handler(aiogram.filters.CommandHelp())
    async def help_handler(message: aiogram.types.Message):
         await message.answer(f"Send me the pic, and i'll try to cartoonify it")

    @dp.message_handler(content_types=[aiogram.types.ContentType.PHOTO])
    async def image_handler(message: aiogram.types.Message):
        if not message.caption:
            return await message.answer('Where is the command?')
        message_caption = message.caption.lower()

        if message_caption in content_handlers:
            handler = content_handlers[message_caption]
            return await handler(message, bot)
        return await message.answer('Unknown command!')

    aiogram.executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    run()