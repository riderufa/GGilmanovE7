1. Создать каталог mkdir.
2. Войти в каталог.
3. Инициировать в нем git командой git init.
4. Скопировать приложение командой git pull https://github.com/riderufa/GGilmanovE7
5. Запустить контейнер mongo командой sudo docker run --name mongo-instance --rm -d -p "27017:27017" mongo:4.2.3
6. Запустить контейнер redis командой sudo docker run --name redis-instance --rm -d -p 6379:6379 redis:5.0.7 redis-server --appendonly yes
7. Создать окружение командой python3 -m venv venv
8. Установить окружение командой pip install -r requirements.txt.
9. Инициировать окружение командой source venv/bin/activate
10. Запустить приложение командой python manage.py runserver