# 1. Цель проекта

Цель проекта — разработать систему напоминания (далее Боте) о домашнихных работах предоставленных к выполнению в виде чат-бота в Телеграм.

Пользователь сможет создавать в Боте заметки с прикреплениями любого формата.

Студент будет получать ежедневное напоминание о собственных заметках до тех пор, пока не удалит их.

# 2. Описание системы

Система состоит из следующих основных функциональных блоков:

1. Регистрация и аутентификация пользователей по Telegram ID
2. Функционал для добавления файлов
3. Функционал для добавления заметок
4. Функционал для поощрения разработчика (донат)

## 2.1 Типы пользователей

Система предусматривает один тип пользователей: студент. Студент может создавать, редактировать и изменять собственные заметки и данные.

## 2.2 Регистрация

На одного пользователя Телеграм создаётся один аккаунт. Таким образом, ведение заметок под разными аккаунтами в рамках одного пользователя не подразумевается.

Бот при регистрации должен принимать следующие данные:

* **Telegram ID** — обязательное поле

Регистрацией является использование команды `/start` в интерфейсе приложения или веб-клиента Телеграм.

При желании пользователь может указать дополнительные поля своего профиля:

* **email** — опциональное поле
* **имя** — опциональное поле

# 2.3 Аутентификация студента

Аутентификация студента осуществляется по Telegram ID. В случае совподения которого пользователю будет предоставлен полный доступ.

# 3. Предлагаемый стек технологий

Для реализации системы предлагается следующий стек технологий:

* Язык Python
* Библиотека [aiogram](https://github.com/aiogram/aiogram) для интеграции с Telegram
* БД SQLite