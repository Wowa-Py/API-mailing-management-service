# API-mailing-management-service
Mailing List Management Service API; implementation: Python/Django

Проект "API-mailing-management-service" является сервисом управления рассылками и предоставляет API для создания рассылок, просмотра созданных рассылок и получения статистики по выполненным рассылкам.

**Требования**

Python 3.12

Docker 

# Шаги по установке и запуску


**Клонируйте репозиторий проекта:**
git clone https://github.com/your_username/your_project.git

**Перейдите в директорию проекта:**
cd service
cd maillind

**Создайте файл .env в корневой директории проекта и укажите необходимые переменные окружения:**
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=your_database_name

DB_USER=your_database_user

DB_PASSWORD=your_database_password

DB_HOST=db

DB_PORT=5432

**Запустите проект с помощью Docker Compose:**
docker-compose up -d --build

**Примените миграции базы данных:**
docker-compose exec web python manage.py migrate

**Создайте суперпользователя:**
docker-compose exec web python manage.py createsuperuser

**Откройте веб-браузер и перейдите по адресу** http://127.0.0.1:8000//admin/ **для доступа к административной панели.**

**Документация по API доступна по адресу** http://127.0.0.1:8000/docs/.

**Чтобы остановить проект, выполните следующую команду:**

docker-compose down

**Используемые технологии**

Redis: Используется в качестве брокера сообщений для Celery, обеспечивая асинхронную обработку задач.

Celery: Используется для выполнения задач в фоновом режиме, таких как отправка сообщений и другие длительные операции.


### Удачи с проектом "API-mailing-management-service"!

Следуйте этим инструкциям, чтобы установить и запустить проект "API-mailing-management-service". Если у вас возникли вопросы или проблемы, обратитесь к разработчику проекта.
