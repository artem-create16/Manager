from aiogram import types
from aiogram.types import CallbackQuery
import logging
from keyboards.inline.buttons import (choice_buttons, first_digit, second_digit)
from keyboards.inline.callback_datas import callback
from loader import dp


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    user = message.from_user.id
    chat = message.chat.id

    await message.reply(f'Привет, {message.from_user.full_name}!\nЧему равно {first_digit} + {second_digit} ?',
                        reply_markup=choice_buttons)


@dp.callback_query_handler(callback.filter(choice_from_new_user=f"{first_digit + second_digit}"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Thanks, human!")


@dp.callback_query_handler(callback.filter(choice_from_new_user="bot"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Sorry, it's not a Detroit")
