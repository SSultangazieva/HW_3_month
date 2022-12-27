# логика FSM

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext #
from aiogram.dispatcher.filters import Text #
from aiogram.dispatcher.filters.state import State, StatesGroup # состояник и шруппы состояний
from keyboards import client_kb
from database.bot_db import sql_command_insert
from config import ADMINS
import uuid


# 1) шаги, что мы будем запрашивать у пользователя: заранее указать последовательность этой дорожной карты:
# группы состояний
class FSMAdmin(StatesGroup): # создаем класс, котораянаследуется от группы состояний StatesGroup
    #создаем объекты класса состояний:
    id = State()
    name = State()
    direction = State()
    age = State()
    gruppa = State()
    photo = State()
    submit = State() # в конце запросит подтверждение


# 2) запустить FSM режим
async def fsm_start(message: types.Message):
    # регистрация должна быть только в личном чате с ботом
    if message.chat.type == 'private' and message.from_user.id in ADMINS:
        #активировать FSM с первого объекта через функцию set() - ЗАПУСТИТЬ FSM режим
        await FSMAdmin.id.set()
        # послать вопрос для заполнения каждого режима:
        await message.answer("Айди ментора?", reply_markup=client_kb.cancel_markup) #
    else:
        await message.answer("Пиши в личке!") # ЗАДАТЬ СЛЕДУЮЩИЙ ВОПРОС ?????????


async def load_id(message: types.Message, state: FSMContext):
    try:
        id = int(message.text)
        async with state.proxy() as data:
            data['id'] = id
        await FSMAdmin.next()
        await message.answer('имя ментора:', reply_markup=client_kb.cancel_markup)
    except:
        await message.answer('Айди только из цифр', reply_markup=client_kb.cancel_markup)
# 3) функция, которая принимает и записывает данные в кэш:
async def load_name(message: types.Message, state: FSMContext):
    # открыть кэш как переменную data
    # там все хранится в типе dict
    async with state.proxy() as data:
        # Создание случайного идентификатора с помощью uuid1()
        # data['id'] = int(uuid. uuid1())
        # можно забрать данные не запрашивая:
        data['username'] = f"@{message.from_user.username}"
        data['name'] = message.text
    # ПЕРЕКЛЮЧИТЬ СОСТОЯНИЕ
    await FSMAdmin.next()
    await message.answer("какое направление у вас?", reply_markup=client_kb.direction_markup)

# 4) следующее состояние:
async def load_direction(message: types.Message, state: FSMContext):
    if message.text not in ["backend", "frontend", "ios/android", "fullstack", "UX-UI"]:
        await message.answer("Выберите из списка!")
    else:
        async with state.proxy() as data:
            data['direction'] = message.text
        await FSMAdmin.next()
        await message.answer("Сколько вам лет?", reply_markup=client_kb.cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    # можно валидацию прописать
    if not message.text.isdigit():
        await message.answer("Пишите только числа")
    elif int(message.text) < 18 or int(message.text) > 45:
        await message.answer("Возростное ограничение!")
    else:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("В какой вы группе?", reply_markup=client_kb.cancel_markup) # reply_markup - кнопки направлений


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gruppa'] = message.text
    await FSMAdmin.next()
    await message.answer("Скиньте фотку?)")

# фото
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # выбрать 0 индекс сжатого фото:
        data['photo'] = message.photo[0].file_id
        # вывести пользователю все данные:
        await message.answer_photo(data['photo'],
                                   caption=f"name: {data['name']}, direction: {data['direction']}, "
                                           f"age: {data['age']}\ngroup: {data['gruppa']}\n{data['username']}")
        # caption отправит как ОПИСАНИЕ ФОТО
    await FSMAdmin.next()
    await message.answer("Все верно?", reply_markup=client_kb.submit_markup)

# попросить подтверждения
async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        # ВНЕСТИ СОБРАННУЮ ИНФУ В БАЗУ ДАННЫХ
        await sql_command_insert(state)
        # после внесени в БД закрыть FSM режим. ВСЕ ЧТО НАПИСАНО ОЧИЩАЕТСЯ
        await state.finish()
        await message.answer("вы зарегистрированы")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Ну как хотите!!!")
    else:
        await message.answer('Чего вы хотите???')

# функция для отмены регистарции
async def cancel_fsm(message: types.Message, state: FSMContext):
    # в переменную приходит состояние пользователя ЕСЛИ ОН НАХОДИТСЯ В КАКОМ-ТО СОСТОЯНИИ
    current_state = await state.get_state()
    # если у пользователя какое-то состояние, то завершает состояние (и внизу регаем с его командой cancel)
    if current_state is not None:
        # ЗАВЕРШИТЬ FSM состояние
        await state.finish()
        await message.answer("Ну как хотите!!!")

# функция регистрации хэндлеров
def register_handlers_fsm_anketa(dp: Dispatcher):
    # зарегать отмену регистарции
    dp.register_message_handler(cancel_fsm, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True), state="*")

    # команда регистарции
    dp.register_message_handler(fsm_start, commands=['reg'])

    # регистация команд состояний
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name) #чтобы группа name работала на состоянии state=FSMAdmin.name
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.gruppa)
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo']) #только фото принимает content_types
    dp.register_message_handler(submit, state=FSMAdmin.submit)
