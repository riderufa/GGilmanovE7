1. Создать каталог mkdir.
2. Инициировать в нем git командой git init.
3. Скопировать приложение в папку appgg командой git pull https://github.com/riderufa/appgg
4. Запустить контейнер mongo командой sudo docker run --name mongo-instance --rm -d -p "27017:27017" mongo:4.2.3
5. Запустить контейнер redis командой sudo docker run --name redis-instance --rm -d -p 6379:6379 redis:5.0.7 redis-server --appendonly yes
6. Открыть приложение по адресу 0.0.0.0:8081.