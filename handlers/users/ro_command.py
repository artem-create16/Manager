import datetime
import re

import aiogram
import asyncio
from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup, AdminFilter
from loader import dp


@dp.message_handler(IsGroup(), Command("ro", prefixes="!"), AdminFilter())
async def ro_command(message: types.message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)

    time = int(time)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
        # await message.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Ошибка! {err.args}")
        return

    await message.answer(f"{message.reply_to_message.from_user.full_name} не сможет писать в чат {time} минут.\n"
                         f"Причина: <b>{comment}</b>")