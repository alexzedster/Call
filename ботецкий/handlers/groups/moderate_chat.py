import asyncio
import datetime
import re

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup, AdminFilter
from loader import dp, bot


@dp.message_handler(IsGroup(), Command("ro", prefixes="/!"), AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r'(!ro|/ro) ?(\d+)? ?([a-zA-Zа-яА-Я ]+)?')
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5
    else:
        time = int(time)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    ReadOnlyPermissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_invite_users=True,
        can_send_polls=False,
        can_pin_messages=False
    )
    try:
        await bot.restrict_chat_member(chat_id=chat_id, user_id=member_id, permissions=ReadOnlyPermissions,
                                       until_date=until_date)
        await message.reply(
            f"Пользователю {member.get_mention()} запрещено писать на {time} минут по причине: {comment}.")
    except BadRequest:
        await message.reply(f"Пользователь является администратором.")

    service_message = await message.reply("Сообщение самоуничтожится через 5 секунд")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command("unro", prefixes="/!"), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_change_info=False,
        can_invite_users=True,
        can_send_polls=False,
        can_pin_messages=False
    )

    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(
        f"Пользователю {member.full_name} разрешено писать")

    service_message = await message.reply("Сообщение самоуничтожится через 5 секунд")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command("ban", prefixes="/!"), AdminFilter())
async def ban(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.kick(user_id=member_id)
    await message.reply(f"Пользователь {member.full_name} был забанен")


@dp.message_handler(IsGroup(), Command("unban", prefixes="/!"), AdminFilter())
async def unban(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.unban(user_id=member_id)
    await message.reply(f"Пользователь {member.full_name} был разбанен")

    service_message = await message.reply("Сообщение самоуничтожится через 5 секунд")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()
