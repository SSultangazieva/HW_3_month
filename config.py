# основные настройки проекта

from aiogram import Bot, Dispatcher
from decouple import config
#подключить инструмент, который подключает кэш к нашему боту:
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#создать объект кэша, на основе класса MemoryStorage
storage = MemoryStorage()


TOKEN = config("TOKEN1")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage) # подключить объект кэша к боту

ADMINS = [5367214519,  1720206106]
# ID Асылбека:
Asylbek = [5022825338]

