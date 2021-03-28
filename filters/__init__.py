from aiogram import Dispatcher

from .check_group import IsGroup
from .check_admins import AdminFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
