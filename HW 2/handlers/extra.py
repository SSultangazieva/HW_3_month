# хранится пустой message_handler, который принимает все подряд
import random

from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
import random


# принцип-DRY - Don't Repeat Yourself
# @dp.message_handler()
async def echo(message: types.Message):
    print(message)

    if message.chat.type != "private":  # в группе (а не в личном чате с ботом)
        bad_words = ['JavaScript', 'html', 'жаман', 'чокун', 'зараза']
        username = f"@{message.from_user.username}" \
            if message.from_user.username is not None else message.from_user.full_name  # если нет username, то full_name

        for i in bad_words:
            if i in message.text.lower().replace(' ', ''):
                # при соблюдении ВСЕХ ВЫШЕПЕРЕЧИСЛЕННЫХ УСЛОВИЙ IFа, УДАЛИТ его сообщение
                await bot.delete_message(message.chat.id, message.message_id)
                # и ОТВЕТИТ заданный текст:
                await message.answer(f"Не матерись {username}, "
                                     f"сам ты {i}!")
    # ЗАКРЕПИТ сообщение начинаещееся на !pin
    #  if message.text.startswith('!pin'):
    #     await bot.pin_chat_message(message.chat.id, message.message_id)

    # ЗАКРЕПИТ сообщение начинаещееся на !pin, то сообщение, на которое отвечено !pin - message.reply_to_message.message_id
    if message.text.startswith('!pin') and message.chat.type != "private":
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

    # if message.text == 'dice':
    #  a = await bot.send_dice(message.chat.id, emoji='🎳')
    # print(a.dice.value)

    if message.text.startswith("game") and message.from_user.id in ADMINS and message.chat.type != "private":
        lst = ["🎳", "🎲", "🎰", "🎯", "⚽", "🏀"]
        random_index = random.randrange(len(lst))
        print(lst[random_index])
        await message.answer(lst[random_index])
        # print(message.from_user.id)

    if message.chat.type == "private":
        if str(message.text).isdigit():
            await bot.send_message(chat_id=message.from_user.id, text=int(message.text) ** 2)
        else:
            await bot.send_message(chat_id=message.from_user.id, text=message.text)


# регистрация функционала
def register_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
