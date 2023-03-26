from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберете товар из меню ниже", reply_markup=menu)


@dp.message_handler(text="Пися")
async def get_piska(message: types.Message):
    await message.answer("Вы выбрали сосать пенис, сосите.")


@dp.message_handler(Text(equals=["Попа", "Писяпопа"]))
async def get_out(message: types.Message):
    await message.answer(f"Вы выбрали неверный вариант! , {message.text}", reply_markup=ReplyKeyboardRemove())

