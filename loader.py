"""Данный модуль создает экземпляр Телеграм бота и таблицы баз данных истории и игровой статистики."""

from telebot import TeleBot
from telebot.storage import StateMemoryStorage

from config_data import config
from database.history.model import Request, Result, User, db

storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
db.create_tables([User, Result, Request], safe=True)

