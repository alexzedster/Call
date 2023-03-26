from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


@dp.message_handler(filters.IsReplyFilter(True), commands='user_id')
async def reply_filter_example(msg: types.Message):
    await msg.answer(msg.reply_to_message.from_user.id)
