import asyncio
from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

FORBIDDEN_PHRASE = [
    'пися',
    'попа',
    'кака',
    'писька',
    'попка',
    'какашка',
    'говняшка'
]
DCP_PHRASE = 'э'


@dp.message_handler(filters.Text(equals=FORBIDDEN_PHRASE, ignore_case=True))
async def forbidden_phrase(message: types.Message):
    await message.reply("ЭТО ТЫ!")


@dp.message_handler(filters.Text(contains=DCP_PHRASE, ignore_case=True))
async def forbidden_phrase(message: types.Message):
    await message.reply("НЕ ЭКАЙ МНЕ ТУТ!")


@dp.message_handler(filters.Text(contains='пака', ignore_case=True))
async def forbidden_phrase(message: types.Message):
    await message.reply("По жопе получишь!")
