import logging

from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api import db_gino


async def on_startup(dispatcher):
    print("Подключаем БД")
    await db_gino.on_startup(dispatcher)
    print("Готово")

    print("Чистим БД")
    await db.gino.drop_all()
    print("Готово")
    print("Создаем таблицы")
    await db.gino.create_all()
    # logging.info("Создаем подключение к базе данных")
    # await db.create()
    # logging.info("Создаем таблицу пользователей")
    # await db.create_table_users()
    # logging.info("Готово.")

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

