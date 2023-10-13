# codeforces__parser
Телеграм бот для парсинга архива задач Codeforces

---

### Описание
- Настроена интеграция со сторонними API: Telegram
- Возможность  получать выборку из Базы данных (10 задач), в зависимости от темы и сложности задачи
- Натсроена периодическая задача через Celery(Каждый час)
- В requirements.txt список зависимостей
  
---

### Технологии
- Python 
- Postgresql
- Django
- интеграция со сторонними API: Telegram, Codeforces
- Celery, Redis
- TelegramBotApi

---

### Запуск приложения в локальной сети:

_Для запуска проекта необходимо клонировать репозиторий и создать и активировать виртуальное окружение:_

```
python3 -m venv venv

source venv/bin/activate
```

_Установить зависимости:_

```
pip install -r requirements.txt
```

_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample_

_Выполнить миграции:_

```
python3 manage.py migrate
```
_Создать администратора:_

```
python3 manage.py createsuperuser
```

_Для заполнения БД запустить команду:_

```
python3 manage.py loaddata data.json
```

_Для запуска redis_:

```
redis-cli
```

_Для запуска celery:_

```
celery -A config worker --loglevel=info
```

_Для запуска django-celery-beat:_

```
celery -A config beat --loglevel=info
```

_Для запуска парсинга:_

```
python3 manage.py fill
```

_Для запуска бота:_

```
python3 manage.py bot
```
