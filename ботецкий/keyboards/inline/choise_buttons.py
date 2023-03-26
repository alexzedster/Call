from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Купить грушу",
                                          callback_data=buy_callback.new(item_name="pear", quantity=1)
                                      ),
                                      InlineKeyboardButton(
                                          text="Купить яблоки",
                                          callback_data="buy:apple:5"
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data="cancel"
                                      )
                                  ]
                              ])


cancel_kb = InlineKeyboardButton(text="Отмена", callback_data="cancel")
pear_keyboard = InlineKeyboardMarkup(row_width=1)
PEAR_LINK = "https://lenta.com/catalog/frukty-i-ovoshchi/frukty/grushi/?utm_referrer=https%3A%2F%2Fwww.google.com%2F"
pear_link = InlineKeyboardButton(text="Купить здесь", url=PEAR_LINK)
pear_keyboard.insert(pear_link)
pear_keyboard.insert(cancel_kb)

apple_keyboard = InlineKeyboardMarkup(row_width=1)
APPLE_LINK = "https://lenta.com/catalog/frukty-i-ovoshchi/frukty/yabloki/"
apple_link = InlineKeyboardButton(text="Купить здесь", url=APPLE_LINK)
apple_keyboard.insert(apple_link)
apple_keyboard.insert(cancel_kb)