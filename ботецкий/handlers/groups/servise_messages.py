from aiogram import types

from filters import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Привет {members}.")


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def left_chat_member(message: types.Message):
    await message.answer(f"{message.left_chat_member.full_name} был удалён из чата "
                         f"пользователем {message.from_user.full_name}.")
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} вышел из чата")
    elif message.from_user.id == bot.me.id:
        return
    else:
        await message.answer(f"{message.left_chat_member.full_name} был удалён из чата "
                             f"пользователем {message.from_user.get_mention(as_html=True)}.")
