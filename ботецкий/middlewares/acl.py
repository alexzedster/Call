from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.db_api.models import User


class ASLMiddleware(BaseMiddleware):
    async def setup_chat(self, data: dict, user: types.User):
        user_id = user.id

        user = User.get_or_create(user_id)
        data["user"] = user

    async def on_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user)

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        await self.setup_chat(data, call.from_user)
