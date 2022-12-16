# хранится пустой message_handler, который принимает все подряд
import random
from aiogram import types, Dispatcher
from config import bot, dp, ADMINS


# принцип-DRY - Don't Repeat Yourself
# @dp.message_handler()
async def echo(message: types.Message):
    have_bad_word = False
    if message.chat.type != "private":
        bad_words = ['JavaScript', 'html', 'жаман', 'чокун', 'зараза']
        username = f"@{message.from_user.username}" \
            if message.from_user.username is not None else message.from_user.full_name  # если нет username, то full_name

        for i in bad_words:
            if i in message.text.lower():
                # при соблюдении ВСЕХ ВЫШЕПЕРЕЧИСЛЕННЫХ УСЛОВИЙ IFа, УДАЛИТ его сообщение
                await bot.delete_message(message.chat.id, message.message_id)
                # и ОТВЕТИТ заданный текст:
                await message.answer(f"Не матерись {username}, "
                                     f"сам ты {i}!")
                have_bad_word = True

    # эхо-бот в приватном чате
    if not have_bad_word:
        if message.text.startswith("game") and message.chat.id in ADMINS:
            lst = ["🎳", "🎲", "🎰", "🎯", "⚽", "🏀"]
            random_index = random.randrange(len(lst))
            # print(lst[random_index])
            await bot.send_dice(message.chat.id, emoji=lst[random_index])
        elif str(message.text).isdigit():
            await bot.send_message(chat_id=message.chat.id, text=int(message.text) ** 2)
        else:
            await bot.send_message(chat_id=message.chat.id, text=message.text)

    # в группе (а не в личном чате с ботом)
    # проверка на плохие слова:


# регистрация функционала
def register_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
