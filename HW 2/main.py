# только запуск программы

from aiogram.utils import executor
from handlers import client, callback, extra, admin
from config import dp
import logging

# запускаем, зареганные функции в др модулях:
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)

# пустой хэндлер должен быть в конце:
extra.register_handler_extra(dp)


# запуск бота:
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
