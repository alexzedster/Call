from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.db_api.models import User
from utils.misc.sentinel import allow_access


@allow_access()
@dp.message_handler(Command("block_me"))
async def block_me(message: types.Message, user: User):
    user.block()
    await message.answer(f"Пользователь имеет статус: {user.allowed}. Теперь доступ запрещен.\n"
                         f"Разблокироваться можно по команде /unblock_me")


@allow_access()
@dp.message_handler(Command("unblock_me"))
async def unblock_me(message: types.Message, user: User):
    user.allow()
    await message.answer(f"Пользователь имеет статус: {user.allowed}. Теперь доступ разрешен.\n"
                         f"Заблокироваться можно по команде /block_me")
