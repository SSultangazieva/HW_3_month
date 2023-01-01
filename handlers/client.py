# функционал связаннй с клиентом (пользователем бота)

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp, ADMINS
from keyboards.client_kb import start_markup
import random
from database.bot_db import sql_command_random
from parser.parser import Parser_Svetofor



# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салам хозяин {message.from_user.first_name}",
                           reply_markup=start_markup)
    # await message.answer("This is an answer method")
    # await message.reply("This is a reply method")


async def info_handler(message: types.Message):
    await message.reply("Сам рабирайся!")


#@dp.message_handler(commands=['mem'])
async def handler(message: types.Message):
    photo = open('media/kurs.jpg', "rb")
    await bot.send_photo(message.from_user.id, photo=photo)


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="NEXT 2")
    markup.add(button_call_1)

    question = "Что делает return?"
    answers = [
        'Возвращает любое значение и выходит из функции',
        'возвращает только список',
        'возвращает только True',
        'возвращает любой тип данных',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        #open_period=5,
        reply_markup=markup
    )

async def pin(message: types.Message):
    # ЗАКРЕПИТ сообщение начинаещееся на !pin
    #  if message.text.startswith('!pin'):
    #     await bot.pin_chat_message(message.chat.id, message.message_id)

    # ЗАКРЕПИТ сообщение, на которое отвечено !pin админом - message.reply_to_message.message_id
    if message.text.startswith('!pin') and message.chat.type != "private":
        if message.reply_to_message:
            # 1) где закреплять 2) какое сообщение закреплять
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        else:
            await bot.send_message(message.chat.id, 'не ответ на сообщение')

async def get_random_user(message: types.Message):
    await sql_command_random(message)



async def get_svetofor(message: types.Message):
    iphone = Parser_Svetofor.parser()
    for i in iphone:
        await message.answer_photo(photo=i['image'], caption=f"{i['name']}\n\n"
            f"{i['link']}\n"
            f"{i['price']}\n"
        )


# регистрация функционала
def register_handlers_client(dp: Dispatcher): #в функцию принимается параметр диспетчер и его тип данных-Dispatcher
    # в зависимости что резистрируем применяем метод, (название функции (без вызова) прописываем команды):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(handler, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(get_svetofor, commands=['svetofor'])


