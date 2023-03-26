from aiogram import types
from aiogram.dispatcher.filters import Text, CommandStart
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton

from data.config import allowed_users
from loader import dp


@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    await query.answer(
        [
            types.InlineQueryResultArticle(
                id="unknown",
                title="Введите какой-то запрос",
                input_message_content=types.InputTextMessageContent(
                    message_text="Не обязательно жать при этом на кнопку"
                )
            )
        ],
        cache_time=5
    )


@dp.inline_handler()
async def some_query(query: types.InlineQuery):
    user = query.from_user.id
    if user not in allowed_users:
        await query.answer(
            results=[],
            switch_pm_text="Бот недоступен. Подключить бота",
            switch_pm_parameter="connect_user",
            cache_time=5
        )
        return

    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Название, которое отображается в инлайн режиме!",
                input_message_content=types.InputTextMessageContent(
                    message_text="Тут будет какой-то <b>текст</b>, который будет отправлен при нажатии на кнопку"
                ),
                url="https://core.telegram.org/bots/api",
                thumb_url="https://avatars.mds.yandex.net/i?id=4e1f2d4e3558109da5e2d5e4d33c7edbcefca924-8496275-images-thumbs&n=13&exp=1",
                description="Описание, в инлайн режиме"
            ),
            # types.InlineQueryResultVideo(
            #     id="4",
            #     video_url="https://shutterstock.7eer.net/c/1203981/43977/1305?u=https://www.shutterstock.com/video/clip-1075031189&&sharedId=collection_page&subId1=staff-picks&subId2=0&subId3=drill_down",
            #     caption="Подпись к видео",
            #     title="Какое-то видео",
            #     description="Какое-то описание",
            #     thumb_url="https://avatars.mds.yandex.net/i?id=1d62f2d43d689fd9aa5ca7bf387c2c26-6500121-images-thumbs&n=13&exp=1",
            #     mime_type="video/mp4"
            # )
        ]
    )


@dp.message_handler(CommandStart(deep_link="connect_user"))
async def connect_user(message: types.Message):
    allowed_users.append(message.from_user.id)
    await message.answer("Вы подключены",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text="Выйти в инлайн режим",
                                                          switch_inline_query_current_chat="Запрос")
                                 ]
                             ]
                         ))