# Пет-проект "Дневник детства"

## Описание
Телеграм-бот, через который пользователь может загрузить детские фотографии и на выходе получить книгу, 
сгенерированную искусственным интеллектом. Книга включает в себя историю в виде текстовой информации в 
формате рассказа разного жанра и сюжета (приключения, комикс, будущая профессия, сказка и т.д.), а также 
описание моментов, которые происходят на фотографиях.

## Установка
Сервис можно запустить с помощью Docker Compose.

1. Склонируйте репозиторий проекта:
```
git clone https://gitlab.com/hilkovich/album_stories.git
```
2. [Зарегистрируйте](https://core.telegram.org/bots#how-do-i-create-a-bot) телеграм бота и сохраните токен.

3. [Создайте каталог](https://yandex.cloud/ru/docs/resource-manager/operations/folder/create) в Yandex Cloud и сохраните id.

4. [Создайте API ключ](https://yandex.cloud/ru/docs/iam/operations/api-key/create) и сохраните его.

5. Создайте файл **.env** в корневом каталоге проекта и укажите переменные окружения:
```
TG_BOT_TOKEN="<tg_token>"
YANDEX_ID_CATALOG="<id_catalog>"
YANDEX_API_KEY="<api_key>"

POSTGRES_USER="<username>"
POSTGRES_PASSWORD="<password>"
POSTGRES_HOST="postgres"
POSTGRES_PORT=5432
POSTGRES_DATABASE="postgres"

RABBIT_USER="<username>"
RABBIT_PASSWORD="<password>"
RABBIT_HOST="rabbitmq"
RABBIT_PORT=5672
```
6. Запустите сервис с помощью Docker Compose.
```
docker-compose up --build
```

## Мотивация
Проект реализован в рамках финального блока My First Data Project 
совместного курса Karpov.Courses и AI Talent Hub «ML Engineering». 

## Автор
Хилькович Николай Федорович

## Лицензия
Этот проект распространяется по лицензии MIT.

## Благодарности
- [AI Talent Hub](https://ai.itmo.ru/)
- [Karpov.Courses](https://karpov.courses/)
