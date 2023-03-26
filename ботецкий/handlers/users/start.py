import logging

import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command, AdminFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from filters import IsPrivate
from filters.test_filter import SomeF
from loader import dp, bot
from utils.db_api.models import User
from utils.misc import rate_limit
from utils.db_api import quick_commands as commands

# @rate_limit(5, key="start")
# @dp.message_handler(CommandStart(), SomeF())
# async def bot_start(message: types.Message, middleware_data, from_filter, user: User):
#     await message.answer(f"Привет, {message.from_user.full_name}! \n{middleware_data=} \n{from_filter=}",
#                          reply_markup=InlineKeyboardMarkup(
#                              inline_keyboard=[
#                                  [
#                                      InlineKeyboardButton(text="Простая кнопка", callback_data="button"),
#                                  ]
#                              ]
#
#                          ))
#     logging.info(f"6. Handler")
#     logging.info("Следующая точка: Post Process Message")
#     return {"from_handler": "Данные из хендлера"}

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await commands.add_user(full_name=message.from_user.full_name,
                                 username=message.from_user.username,
                                 telegram_id=message.from_user.id
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await commands.select_user(telegram_id=message.from_user.id)

    count_users = await commands.count_users()

    user_data = list(user)
    user_data_dict = dict(user)

    username = user.get('username')
    full_name = user[1]

    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f"Ты был занесен в базу",
                f"В базе <b>{count_users}</> пользователей",
                "",
                f"<code>User: {username} - {full_name}",
                f"{user_data=}",
                f"{user_data_dict=}</code>"
            ]
        )
    )


@dp.message_handler(Command('drop'))
async def drop(message: types.Message):
    await commands.drop()
    await message.answer("Таблица удалена")


@dp.message_handler(Command('delete'), AdminFilter())
async def delete(message: types.Message):
    await commands.delete_users()
    await message.answer("Пользователи удалены")


@rate_limit(5)
@dp.callback_query_handler(text='button')
async def bot_posil(callback: types.CallbackQuery):
    await callback.answer(text="ИДИ НАХЕР, ПРИДУРОК АХХААХА", show_alert=True)
    chat_id = callback.message.chat.id
    username = callback.from_user.username
    await bot.send_message(chat_id=chat_id, text=f"@{username} - <code>Этот клоун нажал на кнопку</code>)))) \n(вот "
                                                 f"даун)")
