FROM python:3.12-alpine

# Установка зависимостей для работы с PostgreSQL и Redis
RUN apk add --no-cache postgresql-libs libffi-dev openssl-dev gcc musl-dev redis

# Указываем рабочую директорию внутри контейнера
WORKDIR / mailling
# Копируем все файлы проекта в контейнер
COPY . .
# Копируем файл requirements.txt в контейнер
# COPY requirements.txt .

# Создадим пользователя в системе
RUN adduser --disabled-password service-user

# Установите зависимости
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

USER service-user

# Запускаем Redis
CMD redis-server --daemonize yes && python3 manage.py runserver 0.0.0.0:8000
