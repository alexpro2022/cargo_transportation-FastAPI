# Сервис поиска ближайших машин для перевозки грузов.

REST API сервиc для поиска ближайших машин к грузам.



## Оглавление
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск](#установка-и-запуск)
- [Удаление](#удаление)
- [Автор](#автор)


## Технологии
<details><summary>Развернуть</summary>

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?logo=Pydantic)](https://docs.pydantic.dev/)
[![Uvicorn](https://img.shields.io/badge/-Uvicorn-464646?logo=Uvicorn)](https://www.uvicorn.org/) 

[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)
[![asyncpg](https://img.shields.io/badge/-asyncpg-464646?logo=PostgreSQL)](https://pypi.org/project/asyncpg/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-v2.0-blue?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?logo=alembic)](https://alembic.sqlalchemy.org/en/latest/)

[![docker_hub](https://img.shields.io/badge/-Docker_Hub-464646?logo=docker)](https://hub.docker.com/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?logo=NGINX)](https://nginx.org/ru/)

[⬆️Оглавление](#оглавление)
</details>



## Описание работы

При запуске приложения БД инициализируется следующими данными:
 1. Списком уникальных локаций, представленых в csv файле "uszips.csv". Каждая локация содержит в себе следующие характеристики:
    - город;
    - штат;
    - почтовый индекс (zip);
    - широта;
    - долгота.
 2. Списком из 20 машин. Каждая машина - включает следующие характеристики:
    - уникальный номер (цифра от 1000 до 9999 + случайная заглавная буква английского алфавита в конце, пример: "1234A", "2534B", "9999Z")
    - текущая локация;
    - грузоподъемность (1-1000).
    При создании машин по умолчанию локация каждой машины заполняется случайным образом;

Сервис поддерживает следующие базовые функции:

- Получение информации о конкретной локации по ID.
- Получение списка машин.
- Редактирование машины по ID (локация (определяется по введенному zip-коду));
- Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду);
- Получение списка грузов (локации pick-up, delivery, количество ближайших машин (с подходящей грузоподъемностью) до груза ( =< 450 миль));
- Получение информации о конкретном грузе по ID (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин (с подходящей грузоподъемностью) с расстоянием до выбранного груза);
- Редактирование груза по ID (вес, описание);
- Удаление груза по ID.

[⬆️Оглавление](#оглавление)



## Установка и запуск:

### Предварительные условия:
<details><summary>Развернуть</summary>
Предполагается, что пользователь:
 - установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или на удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:

```bash
docker --version && docker-compose --version
```
</details>
<hr>
<details>
<summary>Локальный запуск</summary> 

1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):

```bash
git clone https://github.com/alexpro2022/cargo_transportation-FastAPI.git && \
cd cargo_transportation-FastAPI && \
cp env_example .env && \
nano .env
```

2. Из корневой директории проекта выполните команду:
```bash
docker compose -f infra/local/docker-compose.yml up -d --build
```
Проект будет развернут в трех docker-контейнерах (db, web, nginx) по адресу http://localhost.
Администрирование приложения может быть осуществлено через Swagger доступный по адресу http://localhost/docs .

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose -f infra/local/docker-compose.yml down
```
Если также необходимо удалить том базы данных:
```bash
docker compose -f infra/local/docker-compose.yml down -v
```
<hr>

Для создания тестовых грузов можно воспользоваться следующими данными:

```json
{
  "delivery_zip": "00602",
  "current_zip": "00601",
  "description": "description",
  "weight": 100
}
```

```json
{
  "delivery_zip": "33556",
  "current_zip": "15049",
  "description": "description",
  "weight": 500
}
```

[⬆️Оглавление](#оглавление)

</details></details><hr>



## Удаление:
Для удаления проекта выполните следующие действия:
```bash
cd .. && rm -fr cargo_transportation-FastAPI
```
  
[⬆️Оглавление](#оглавление)


## Автор
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#сервис-поиска-ближайших-машин-для-перевозки-грузов.)



