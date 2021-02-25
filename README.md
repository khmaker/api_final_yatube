# API для Yatube
полноценное API для проекта Yatube

## Функционал

* Подписка на пользователей
* Просмотр, создание, удаление и модификация постов
* Просмотр и создание групп
* Просмотр, создание, удаление и модификация комментариев
* Фильтрация по полям

## Установка

*Для работы с проектом в системе должен быть установлен Python версии 3.6 и выше.*

В директории со скачанным проектом нужно запустить и командную оболочку и выполнить следующие команды:

### Установка [виртуального окружения](https://docs.python.org/3/library/venv.html)
```shell
python -m venv venv
```

### Активация виртуального окружения
#### команда для Linux
```shell
source venv/Scripts/activate
```
#### команда для windows
```shell
venv\Scripts\activate
```

### Установка зависимостей
```shell
pip install -r requirements.txt
```


## Запуск

```shell
python manage.py runserver
```

## Использование

После запуска сервера вам будет доступна [документация](http://localhost:8000/redoc/)

## Технологии
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [DRF Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
