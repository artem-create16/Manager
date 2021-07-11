import asyncio
from aiogram import types
from aiogram.types import CallbackQuery
import logging
from keyboards.inline.buttons import (choice_buttons, first_digit, second_digit)
from keyboards.inline.callback_datas import callback
from loader import dp
import random


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    user = message.from_user.id
    chat = message.chat.id
    random.shuffle(choice_buttons)

    await message.chat.restrict(
        message.from_user.id,
        permissions=types.ChatPermissions(can_send_messages=False))

    await message.reply(f'Привет, {message.from_user.full_name}!\n{first_digit} + {second_digit} ?',
                        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[choice_buttons]))


@dp.callback_query_handler(callback.filter(choice_from_new_user=f"{first_digit + second_digit}"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    callback_data = call.data
    await call.message.chat.restrict(
        call.from_user.id,
        permissions=types.ChatPermissions(can_send_messages=True))
    await call.message.delete()


@dp.callback_query_handler(callback.filter(choice_from_new_user="bot"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    # await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.answer("Wrong answer", show_alert=True)
