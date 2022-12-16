# основные настройки проекта

from aiogram import Bot, Dispatcher
from decouple import config


TOKEN = config("TOKEN1")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

ADMINS = [5367214519,  1720206106]

