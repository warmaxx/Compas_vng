![compas workflow](https://github.com/warmaxx/Compas/actions/workflows/compas_workflow.yml/badge.svg)
![](https://github.com/warmaxx/Compas/blob/master/compas.gif?raw=true)
# Проект КОМПАС
### Система учета работы внутренней службы
Проект копируется в ваш репозиторий и разворачивается на вашем сервере с помощью следующих технологий:
После успешной установки вам отправляется сообщение в телеграмм
## Технологии
* Python 3.7
* Django 2.2.8
* Docker 20.10.10
* Docker-compose
* Telegram
* Postgres
* Hub.docker.com
* Яндекс.Облако
## Описание backend проекта
Проект содержит следующие модули:
`Телефонный справочник`, `Новости`, `Инциденты`.
 

## Права доступа
* `Аноним` - может просматривать все модули.
* `Аутентифицированный пользователь` - может читать всё, как и `Аноним`, а также редактировать свои данные.
* `Модератор` - те же права, что и у `Аутентифицированного пользователя`, плюс право удалять и редактировать любые данные в системе.
* `Администратор` - полные права на управление всем контентом проекта. Может назначать роли пользователям.
## Как запустить проект:
Вам необходимо получить доступ к вашему серверу по SSH, установить docker-compose, зарегистрироваться в Телеграмм, создать вашего бота в телеграмм, зарегистрироваться на DockerHub
### Клонировать репозиторий и перейти в него в командной строке:  

 - [ ] `git clone https://github.com/warmaxx/compas.git`

### Добавить Secrets в свой репозиторий GitHub 
 - [ ] DB_ENGINE # django.db.backends.postgresql - указываем, что работаем с postgresql
 - [ ] DB_HOST # db - название сервиса (контейнера)
 - [ ] DB_NAME # compas_db - имя базы данных
 - [ ] DB_PORT # 5432 - порт для подключения к БД 
 - [ ] DOCKER_USERNAME # Пользователь на hub.docker.com
 - [ ] DOCKER_PASSWORD # Пароль на hub.docker.com
 - [ ] HOST # Хост, на котором нужно развернуть приложение
 - [ ] USER # Пользователь который подключается к Хосту
 - [ ] SSH_KEY # Приватный ключ пользователя
 - [ ] PASSPHRASE # Кодовая фраза, при наличии
 - [ ] POSTGRES_USER # Пользователь в СУБД
 - [ ] POSTGRES_PASSWORD # Пароль пользователя в CУБД
 - [ ] TELEGRAM_TO # ID пользователя которому нужно отправить сообщение
 - [ ] TELEGRAM_TOKEN # Токен Бота, который отправит сообщение
 
### Запустите github-actions workflow:

 - [ ] На странице actions запустите workflow

##Подключитесь к вашему серверу и выполните следующие команды: 
### Выполнить миграции:

 - [ ] `docker-compose exec web python manage.py migrate`

### Создать суперпользователя:

 - [ ] `docker-compose exec web python manage.py createsuperuser`

### Собрать статику:

 - [ ] `docker-compose exec web python manage.py collectstatic`


### Проверить проект:
- [ ] `Перейти на адрес http:\\ваш-сервер\admin\`
- [ ] `Авторизовать под суперпользователем`
- [ ] `Добавить данные`

## Автор:
Максягин Алексей
### Пример работы:
maksyag.in
