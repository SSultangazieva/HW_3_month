# функционал связаннй с администратором

from aiogram import types, Dispatcher
from config import bot
from config import ADMINS


async def ban(message: types.Message):
    # выбираем чат: группу
    if message.chat.type != "private":
        # выбираем того, что может банить: Админ
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        # проверка что это ответ на сообщение reply_to_message
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        # блокировка kick_chat_member
        else:
            await bot.kick_chat_member(message.chat.id, # откуда его баним (группа)
                                       message.reply_to_message.from_user.id) # id кого мы баним
            # или ban_chat_member() - банит, а не просто выгоняет пользователя
            await message.answer(f"Этот {message.from_user.first_name} чел  кикнул "
                                 f"тебя: {message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группе!")

# регистрация функционала
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
