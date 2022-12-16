# keyboard=buttons - закрепленные кнопки внизу экрана

# 1)импортируем:
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# ReplyKeyboardMarkup - блок из кнопок
# KeyboardButton - одна кнопка

# 2) создаем объект класса ReplyKeyboardMarkup - т.е. создан блок кнопок
start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True, # зменить размер (True сжать по форме кнопки)
    one_time_keyboard=True, #чтоб после нажатия клава скрывалась
    row_width=3  #сколько кнопок в одной строке
)
# 3) создаем кнопки:
start_button = KeyboardButton("/start") # параметр - назавание кнопки
info_button = KeyboardButton("/info")
quiz_button = KeyboardButton("/quiz")
mem_button = KeyboardButton("/mem")
#т.к. такие команды start,info,quiz уже есть - эти команды выполняют их функционал.

#   СПЕЦИАЛЬНЫЕ кнопки:
# кнопка для того чтобы поделиться локацией:
share_location = KeyboardButton("Share location", request_location=True)
# кнопка для того чтобы поделиться своим контактом:
share_contact = KeyboardButton("Share contact", request_contact=True)

# кнопки с нуля со своим функционалом: ПОТОМ УЗНАЮ?????????




# 4) добавляем кнопки для блока кнопок:  (т.е. блок кнопок будет состоять из этих кнопок)
start_markup.add(start_button, info_button, quiz_button,
                 share_location, share_contact,mem_button)
#количество кнопок в строке можно контролировать через каждый отдельный add()