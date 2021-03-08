from random import randint
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import callback

first_digit = randint(0, 10)
second_digit = randint(0, 10)

first_choice_for_bot = randint(10, 20)
second_choice_for_bot = randint(0, 9)

choice_buttons = InlineKeyboardMarkup(row_width=3)

choice_human = InlineKeyboardButton(text=f"{first_digit + second_digit}",
                                    callback_data=callback.new(choice_from_new_user=f"{first_digit + second_digit}"))
choice_buttons.insert(choice_human)

choice_bot = InlineKeyboardButton(text=f"{first_choice_for_bot}", callback_data="choice:bot")
choice_buttons.insert(choice_bot)

choice_bot = InlineKeyboardButton(text=f"{second_choice_for_bot}", callback_data="choice:bot")
choice_buttons.insert(choice_bot)
