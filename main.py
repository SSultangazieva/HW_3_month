from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor  #executor файл, внутри которого есть методы запуска бота. Чтобы бот запустился и вышел в онлайн
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config #чтобы скрыть токен бота в файле .env
import logging

TOKEN = config("TOKEN")

'''на основе класса Bot создается объект бота. С помощью этого объекта мы подключаемся к самому боту, через токен. а также с помощью этого объекта управлять ботом'''
bot = Bot(TOKEN) # создаем объект класса Бота, наш код понимает с каким аккаунтом бота работает. принимает токен.

'''Dispatcher принимает входящие сообщения, и туда мы будем регистрировать функции, которые будут отвечать на сообщения'''
dp = Dispatcher(bot=bot)  # создаем объект класса Диспечер, с его помощью принимать будем сообщения. он принимает самого бота.


@dp.message_handler(commands=['start', 'hi'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Приветсвую тебя {message.from_user.first_name}")


@dp.message_handler(commands=['question'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "На 2-х руках 10 пальцев. Сколько пальцев на 10 руках?"
    answers = [
        '50',
        '100',
        '20',
        '10',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=20,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):

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
        open_period=15,

    )

@dp.message_handler(commands=['mem'])
async def start_handler(message: types.Message):
    photo = open('media_files/kurs.jpg', "rb")
    await bot.send_photo(message.from_user.id, photo=photo)



@dp.message_handler()
async def echo(message: types.Message): #строгая типизация типа данных Message, тогда высветятся методы
    #print(str(message.text))
    if str(message.text).isdigit():
        await bot.send_message(chat_id=message.from_user.id, text=int(message.text)**2)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':  #проверка запускается ли именно этот файл
    logging.basicConfig(level=logging.INFO)
    #файл запускается через executor у него метод start_polling
    executor.start_polling(dp, skip_updates=True) #skip_updates пропускать обновления (когда бот отключится и включится: True-не ответит на пропущенные сообщения.  False-ответит)