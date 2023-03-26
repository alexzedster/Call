from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=
[
    [
        KeyboardButton(text="Пися")
    ],
    [
        KeyboardButton(text="Попа"),
        KeyboardButton(text="Писяпопа"),
    ],
],
    resize_keyboard=True
)
