from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .test_filter import SomeF
from .private_chat import IsPrivate
from .admin import AdminFilter
from .group_chat import IsGroup
if __name__ == "filters":
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(SomeF)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)

