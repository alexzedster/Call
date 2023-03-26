import logging

from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choise_buttons import choice, pear_keyboard, apple_keyboard
from loader import dp, bot


@dp.message_handler(commands=['items'])
async def show_items(message: types.Message):
    await message.answer(text="На продажу есть 2 товара: 5 яблок и 1 груша. \n"
                              "Если вам ничего не нужно - жмите отмену",
                         reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="pear"))
async def buying_pear(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    quantity = int(callback_data['quantity'])
    await call.message.answer(f"Вы выбрали купить грушу. Груш всего {quantity}. Спасибо.",
                              reply_markup=pear_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apple(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    quantity = int(callback_data['quantity'])
    await call.message.answer(f"Вы выбрали купить яблоки. Яблок всего всего {quantity}. Спасибо.",
                              reply_markup=apple_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel_def(call: types.CallbackQuery):
    await call.answer(text="Вы отменили покупку", show_alert=True, cache_time=60)
    logging.info("сработало дерьмо")
    await call.message.edit_reply_markup()
    logging.info("Какого хера")
