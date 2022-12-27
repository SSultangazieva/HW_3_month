# callback_query_handler - перехватчик нажатия на кнопку

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


# @dp.callback_query_handler(text="NEXT 2")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="NEXT 3")
    markup.add(button_call_1)

    question = "На 2-х руках 10 пальцев. Сколько пальцев на 10 руках?"
    answers = [
        '50',
        '100',
        '20',
        '10',
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=15,
        reply_markup=markup
    )

# @dp.callback_query_handler(text="NEXT 3")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 3", callback_data="NEXT 4")
    markup.add(button_call_1)

    question = "Функция randit(1,10) выведет?"
    answers = [
        '1',
        '10',
        'ничего, нужен print()',
        'случайное число от 1 до 10'
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )

# вопрос последний, поэтому нет параметров кнопок!!!!
# @dp.callback_query_handler(text="NEXT 4")
async def quiz_4(call: types.CallbackQuery):
    question = "Что легче 1кг ваты или 1 кг железа?"
    answers = [
        "Железо",
        "Вата",
        "Одинаково",
        "Понятия не имею!!!",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        # open_period=5,
    )

# регистрация функционала
def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="NEXT 2")
    dp.register_callback_query_handler(quiz_3, text="NEXT 3")
    dp.register_callback_query_handler(quiz_4, text="NEXT 4")
    #dp.register_callback_query_handler(quiz_3, text="NEXT 4")
