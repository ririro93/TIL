# django
> [blog](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
[blog2](https://github.com/psycopg/psycopg2/issues/684)
- docker-compose up -d --build
  - --build를 넣어줘야지 이미지를 새로 빌드해서 전에 쓰던 db가 반영된다

<br>

## Dockerfile
example dockerfile
```
FROM python:3.8.7-alpine3.13

# Working directory
WORKDIR /usr/src/app

# set env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
COPY requirements.txt /app/requirements.txt
RUN set -ex \
    && pip install --upgrade pip \  
    && pip install --no-cache-dir -r /app/requirements.txt 

# copy entrypoint.sh -> 밑에서 모든 파일 다 복사하지만 이렇게 안하면 밑에꺼가 실행이안됨ㅎㅎ..
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
```

`PYTHONDONTWRITEBYTECODE`: Prevents Python from writing pyc files to disc (equivalent to `python -B` option)
`PYTHONUNBUFFERED`: Prevents Python from buffering stdout and stderr (equivalent to `python -u` option)

<br>

## docker-compose.yml
```
version: '3.8'

services:
  web:
    build: ./crawling_site
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./crawling_site/:/usr/src/app/
    ports:
      - 8000:8000
    env_file:
      - ./.env.dev
  db:
    image: postgres:12.0-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment: 
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=postgres
    ports:
      - 5432:5432
  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=ririro93@gmail.com
      - PGADMIN_DEFAULT_PASSWORD=password
    ports:
      - 80:80

volumes:
  postgres_data:
```