from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware

from .big_brother import BigBrother
from .acl import ASLMiddleware
from .sentinel import Sentinel

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ASLMiddleware())
    dp.middleware.setup(Sentinel())
    dp.middleware.setup(BigBrother())
