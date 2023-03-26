from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("menu", "Посмотреть меню"),
            types.BotCommand("items", "Покупочки"),
            types.BotCommand("set_photo", "Задать фото"),
            types.BotCommand("set_title", "Задать название чата"),
            types.BotCommand("set_description", "Установить описание группы"),
            types.BotCommand("ro", "Режим Read Only"),
            types.BotCommand("unro", "Отключить RO"),
            types.BotCommand("bun", "Забанить"),
            types.BotCommand("unbun", "Разбанить"),
            types.BotCommand("channels", "Список каналов для подписки"),
            types.BotCommand("create_post", "предложить пост в канал"),
            types.BotCommand("show_on_map", "Показать ближайшие магазины"),
            types.BotCommand("callback", "Заказать обратный звонок")
        ]
    )
