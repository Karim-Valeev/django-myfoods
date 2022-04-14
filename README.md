# MyFoods  
### Work in progress...  
Food shopping site made using: Django, DRF, Celery, Docker, PostgeSQL, Redis.  
It remains to finish the main functionality, layout and add tests.  
Django course repo: https://gitlab.com/atnartur.uni/web-monitoring  
DevOps course repo: https://github.com/42praktika/DevOps-Course

### Запуск

- `python3 -m venv env` - создать виртуальное окружение (не забудьте создать файлик .env с вашими переменными окружения)
- `source env/bin/activate` - войти в виртуальное окружение 
- `pip install -r requirements.txt` - установка зависимостей
- `docker-compose -f docker-compose.prod.yml up --build -d` - сборка проекта
- `python src/manage.py migrate` - применить миграции
- `python src/manage.py collectstatic` - собрать всю статику в одну папку
- `pip3 install pre-commit && pre-commit install` - включение pre-commit hook для автоматического запуска линтера
- `python src/manage.py runserver` - запуск сервера для разработки

### Загрузка данных

- `python src/manage.py loaddata src/main/fixtures/*.json` - загрузка начальных данных

### Запуск тестов

- `pytest -n 2 src` - запуск всех тестов в папке src на двух ядрах
