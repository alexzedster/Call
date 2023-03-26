import asyncio

from data import config
from utils.db_api import quick_commands
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRESS_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print("Добавляем пользователей")
    await quick_commands.add_user(1, "One", "email")
    await quick_commands.add_user(2, "two", "@.com")
    await quick_commands.add_user(3, "pidr", "sobaka")
    await quick_commands.add_user(4, "kaloed", "dotcom")
    await quick_commands.add_user(5, "mraz", "mraz.com")
    print("Готово")

    users = await quick_commands.select_all_users()
    print(f"Получил всех пользователей: {users}")

    count_users = await quick_commands.count_users()
    print(f"Всего пользователей: {count_users}")

    user = await quick_commands.select_user(id=1)
    print(f"Получил пользователя: {user}")

loop = asyncio.get_event_loop()
loop.run_until_complete(test())