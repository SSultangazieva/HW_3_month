''''''
# Импорт нужно делать только здесь все в начале (для понимания я их спустила)
# можно через запятую импортировать несколько:   from aiogram import Bot, Dispatcher, types
# '''

#from decouple import config TOKEN = config("TOKEN")
#чтобы скрыть токен бота в файле .env
TOKEN = "5830047027:AAFwZTkzZ6DnhlN27j0NtNIGz6sHrH7JKaE"
#
# from aiogram import Bot
# # создаем объект класса Бота, наш код понимает с каким аккаунтом бота работает. принимает токен.
# bot = Bot(TOKEN)
#
#
# from aiogram import Dispatcher
# # создаем объект класса Диспечер, с его помощью принимать будем сообщения. он принимает самого бота.
# dp = Dispatcher(bot=bot)
#
#
# from  aiogram import types
#
#
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# # InlineKeyboardButton
# # InlineKeyboardMarkup
#
#
#
# @dp.message_handler(commands=['start', 'help']) # можно пустую, одну или несколько команд для одного действия:start,help
# async def start_handler(message: types.Message): #строгая типизация типа данных Message, тогда высветятся методы
#     await bot.send_message(chat_id=message.from_user.id, # обяз.параметр: КУДА отправить
#                            text=f"Салам хозяин {message.from_user.first_name}") # обяз.параметр: ЧТО отправить
#
#     # без метода send_message, ситакс. сахар для отправки к боту сообщений:
#     await message.answer("This is an answer method") #по message понимает куда, поэтому только один параметр
#     await message.reply("This is a reply method")  #как ответ на сообщение ответит
#
#
# # кнопки тоже тип данных в aiogram, поэтому их нужно импортровать:
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# # InlineKeyboardButton - одна кнопка
# # InlineKeyboardMarkup - блок из кнопок
#
# @dp.message_handler(commands=['quiz'])
# async def quiz_1(message: types.Message):
#     # создаем объект класса InlineKeyboardMarkup - т.е. создан блок кнопок
#     markup = InlineKeyboardMarkup()
#     # создаем кнопку
#     # 1 параметр: название кнопки, 2 параметр: перехватчик нажатия кнопки (т.е. другая функция,которая вызывает другой вопрос)
#     button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
#     # в блок markup добавить кнопку button_call_1
#     markup.add(button_call_1)
#
#     question = "На 2-х руках 10 пальцев. Сколько пальцев на 10 руках?"
#     answers = ['50','100','20','10']
#
#     await bot.send_poll(
#         chat_id=message.from_user.id, #куда отправить
#         question=question,  #сам вопрос
#         options=answers,  # варианты ответов
#         is_anonymous=False,  # просто убрать не нужный параметр
#         type='quiz',  #тип опросника: викторина (т.е. с правильным ответом)
#         correct_option_id=1,  #правильный ответ (указать индекс)
#         explanation="Стыдно не знать",  #мини сообщение или подсказка, которое будет высвечиваться
#         open_period=5,  #время для ответа в секундах
#         reply_markup=markup  # ПРИВЯЗАТЬ К ВИКТОРИНЕ БЛОК КНОПОК
#     )
#
# # здесь нет команд, есть аргумент text= которому должен быть подставлен callback_data="button_call_1"
# @dp.callback_query_handler(text="button_call_1")
# async def quiz_2(call: types.CallbackQuery):
#     markup = InlineKeyboardMarkup()
#     button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_2") #для перехода на 3 кнопку
#     markup.add(button_call_1)
#
#     question = "By whom invented Python?"
#     answers = ["Harry Potter","Griffin","Guido Van Rossum","Voldemort","Griffin","Linus Torvalds"]
#     await bot.send_poll(
#         chat_id=call.from_user.id,
#         question=question,
#         options=answers,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=2,
#         explanation="Стыдно не знать",
#         open_period=5,
#         reply_markup=markup
#     )
#
# # переход на 3 кнопку через button_call_2. КНОПОК НЕТ, потому что последник вопрос
# @dp.callback_query_handler(text="button_call_2")
# async def quiz_3(call: types.CallbackQuery):
#     question = "АТВИЧАЙ"
#     answers = ['4','8','4, 6',"2, 4",'5']
#
#     photo = open("media/problem1.jpg", "rb") #указать путь и формат открытия
#     # фото отправляется через метод send_photo
#     await bot.send_photo(call.from_user.id, photo=photo)
#
#     await bot.send_poll(
#         chat_id=call.from_user.id,
#         question=question,
#         options=answers,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=3,
#         explanation="Стыдно не знать",
#         # open_period=5,
#     )
#
# # т.к. библиотека асинхронна, нужно когда объявляем функцию написать async def
# # а при отправке сообщения боту await, каждому сообщению
# @dp.message_handler()
# async def echo(message: types.Message):
#     print(message)
#     await bot.send_message(chat_id=message.from_user.id, text=message.text)
#
#
# import logging
# from aiogram.utils import executor
# #executor файл, внутри которого есть методы запуска бота. Чтобы бот запустился и вышел в онлайн
#
# if __name__ == '__main__':  #проверка запускается ли именно этот файл
#     logging.basicConfig(level=logging.INFO)
#     # наш код запускается и выходит на онлайн через executor у него метод start_polling
#     executor.start_polling(dp, skip_updates=True)
    # skip_updates пропускать обновления (когда бот отключится и включится: True-не ответит на пропущенные сообщения.  False-ответит)'''