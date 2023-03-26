from aiogram import types
from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), user_id=977829670, text="secret")
async def private(message: types.Message):
    await message.answer("Это секретное сообщение для администраторов в личной переписке")
