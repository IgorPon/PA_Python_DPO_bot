"""Модуль обрабатывающий сообщения пользователя при выбранной команде bestdeal.

Functions:
    enter_min_price: Ввод минимальной стоимости проживания
    enter_max_price: Ввод максимальной стоимости проживания
    enter_min_distance: Ввод минимального расстояния до центра
    enter_max_distance: Ввод максимального расстояния до центра
"""
from telebot.types import Message

from config_data.config import COMMAND_MESSAGES
from loader import bot
from states.search_data import UserSearchState
from states.users import Users

from .common_search_handlers import ask_number_of_hotels


@bot.message_handler(func=lambda message: message.text not in COMMAND_MESSAGES, state=UserSearchState.min_price)
def enter_min_price(message: Message) -> None:
    """Получает и проверяет минимальную стоимость проживания, введенную пользователем.

    Запрашивает максимальную стоимость.
    """
    if message.text.isdigit():
        Users.get_user(message.from_user.id).min_price = int(message.text)
        bot.set_state(message.from_user.id, UserSearchState.max_price, message.chat.id)
        bot.send_message(message.chat.id, "Введите максимальную стоимость проживания за ночь")
    else:
        bot.send_message(message.chat.id, "Минимальная стоимость должна быть числом больше 1. Повторите ввод")
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)


@bot.message_handler(func=lambda message: message.text not in COMMAND_MESSAGES, state=UserSearchState.max_price)
def enter_max_price(message: Message) -> None:
    """Получает и проверяет максимальную стоимость проживания, введенную пользователем.

    Запрашивает минимальное расстояние от центра
    """
    user = Users.get_user(message.from_user.id)
    if message.text.isdigit():
        user.max_price = int(message.text)
        bot.send_message(
            message.chat.id, "Выбран диапазон цен: ${min}-{max}".format(min=user.min_price, max=user.max_price)
        )
        bot.set_state(message.from_user.id, UserSearchState.min_distance, message.chat.id)
        bot.send_message(message.chat.id, "Введите минимальное расстояние от центра до отеля")
    else:
        bot.send_message(message.chat.id, "Максимальная стоимость должна быть числом больше 1. Повторите ввод")
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)


@bot.message_handler(func=lambda message: message.text not in COMMAND_MESSAGES, state=UserSearchState.min_distance)
def enter_min_distance(message: Message) -> None:
    """Получает и проверяет минимальное расстояние от центра, введенное пользователем.

    Запрашивает максимальное расстояние от центра
    """
    if message.text.isdigit():
        Users.get_user(message.from_user.id).min_distance = int(message.text)
        bot.set_state(message.from_user.id, UserSearchState.max_distance, message.chat.id)
        bot.send_message(message.chat.id, "Введите максимальное расстояние от центра до отеля")
    else:
        bot.send_message(message.chat.id, "Минимальное расстояние должно быть числом. Повторите ввод")
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)


@bot.message_handler(func=lambda message: message.text not in COMMAND_MESSAGES, state=UserSearchState.max_distance)
def enter_max_distance(message: Message) -> None:
    """Получает и проверяет максимальное расстояние от центра, введенное пользователем.

    Запрашивает требуемое количество отелей
    """
    user = Users.get_user(message.from_user.id)
    if message.text.isdigit():
        user.max_distance = int(message.text)
        bot.send_message(message.chat.id, f"Расстояние от центра: {user.min_distance}-{user.max_distance} миль")
        ask_number_of_hotels(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, "Максимальное расстояние должно быть числом. Повторите ввод")
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
