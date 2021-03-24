from random import randint
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import callback


first_digit = randint(0, 10)
second_digit = randint(0, 10)

first_choice_for_bot = randint(10, 20)
second_choice_for_bot = randint(0, 9)

while first_digit + second_digit == first_choice_for_bot or first_digit + second_digit == second_choice_for_bot:
    if first_digit + second_digit == first_choice_for_bot:
        first_choice_for_bot = randint(10, 20)
    elif first_digit + second_digit == second_choice_for_bot:
        second_choice_for_bot = randint(0, 9)

choice_buttons = [
    types.InlineKeyboardButton(f"{first_digit + second_digit}", callback_data=callback.new(
        choice_from_new_user=f"{first_digit + second_digit}")),
    types.InlineKeyboardButton(f"{first_choice_for_bot}", callback_data=callback.new(choice_from_new_user="bot")),
    types.InlineKeyboardButton(f"{second_choice_for_bot}", callback_data=callback.new(choice_from_new_user="bot")),
]
