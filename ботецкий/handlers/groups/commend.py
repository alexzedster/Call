from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


@dp.message_handler(content_types='photo')
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def content_type_example(message: types.Message):
    await message.answer('Классная фотка! 😍')
