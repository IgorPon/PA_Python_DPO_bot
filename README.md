## Основные функции

* Поиск отелей в заданном городе на указанные даты с сайта [Hotels.com](https://www.hotels.com/)
  * самых дешевых
  * самых дорогих
  * лучших по критериям - стоимость за ночь и расстояние от центра
* Отображение информации по результатам поиска
  * Фотографии отеля
  * Название со ссылкой на сайт [Hotels.com](https://www.hotels.com/)
  * Адрес
  * Расстояние до центра (миль)
  * Стоимость за ночь (USD)
  * Количество ночей
  * Общая стоимость (USD с учетом налогов)
  * Оценка отеля на сайте [Hotels.com](https://www.hotels.com/)
* Выбор параметров вывода результатов
  * максимальное количество результатов поиска
  * количество фотографий
* Сохранение истории поиска
  * Просмотр последних 10 запросов пользователя
  * Возможность повтора запроса

**_! Поиск по городам России на сайте [Hotels.com](https://www.hotels.com/) не предусмотрен_**

## Установка и настройка

1. Настройте виртуальное окружение
2. Установите зависимости в виртуальное окружение:
```commandline
pip install -r requirements.txt
```
3. Переименуйте файл `env.template` в `.env`

Заполните в файле `.env` ваш (администратора) Telegram id и придумайте пароль. 
Данная информация потребуется для очистки баз данных
```dotenv
ADMIN_ID = " "
ADMIN_PASSWORD = " "
```

4. Зарегистрируйте вашего телеграм-бота
* Для регистрации нового бота запустите в Telegram бота [BotFather](https://t.me/botfather) и отправьте команду:
```commandline
/newbot
```

* Введите название бота, которое будет отображаться у пользователя
* Введите имя бота, оканчивающееся на "bot" (например "EasyTravelBot").
Если имя уже занято, Вам будет предложено ввести новое
* Из сообщения об успешном создании бота скопируйте токен в файл `.env`. В результате должна получиться строка вида:
```dotenv
BOT_TOKEN=' '
```
* Дополнительно можно настроить бота, с помощью команды в чате с ботом [BotFather](https://t.me/botfather)
```commandline
/mybots
```
Подробную информацию о настройках и возможностях телеграм-ботов можно получить [здесь](https://core.telegram.org/bots#6-botfather) 

5. Получите доступ к API сайта Hotels.com
* Пройдите регистрацию на сайте [RapidAPI](https://rapidapi.com/auth/sign-up?referral=/apidojo/api/hotels4/)
* Оформите подписку по ссылке [API Hotels](https://rapidapi.com/apidojo/api/hotels4/pricing)
* На странице [API Hotels](https://rapidapi.com/apidojo/api/hotels4/)
скопируйте ключ доступа к API из поля X-RapidAPI-Key в файл `.env`. 
В результате должна получиться строка вида: 
```dotenv
RAPID_API_KEY = " "
```

7. Запустите бота командой
```commandline
python main.py
```

## Используемые Python Packages
* Python 3.9
* pyTelegramBotAPI 4.8.0
* python-dotenv 0.19.2
* requests 2.28.1
* python-telegram-bot-calendar 1.0.5
* python-telegram-bot 13.15
* loguru 0.6.0
* translators 5.5.5
* peewee 3.15.4

## Работа телеграм-бота
### Начало работы
Для начала работы отправьте боту команду `/start`

### Поиск отелей
Для поиска отелей выберите один из предложенных вариантов поиска
в меню или с помощью команд:
* `/lowprice` - вывод самых дешевых отелей
* `/highprice` - вывод самых дорогих отелей
* `/bestdeal` - вывод отелей, наиболее подходящих по цене и расположению от центра

Далее вводите информацию по запросам бота
### История запросов
При вводе команды `/history` бот покажет последние 10 запросов. 
Для каждого запроса можно показать результаты или повторить запрос.

## Базы данных
Для хранения истории запросов пользователей используется база данных SQLite

Для отчистки базы данных истории запросов введите команду в телеграм боте `/clear`.
Далее действуйте согласно запросам бота