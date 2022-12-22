# только запуск программы

from aiogram.utils import executor
from handlers import client, callback, extra, admin, fsm_anketa
from config import dp
import logging
from database.bot_db import sql_create

# запускаем, зареганные функции в др модулях:
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)

fsm_anketa.register_handlers_fsm_anketa(dp)

# пустой хэндлер должен быть в конце:
extra.register_handler_extra(dp)


# запуск создания БД
async def on_startup(_):
    sql_create()


# запуск бота:
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    # on_startup=on_startup - чтобы эта функция запускалась в момент запуска бота
