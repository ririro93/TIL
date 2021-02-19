# reset migrations
>[blog](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)

1. rm all migration files
    ```
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete
    ```
2. delete `db.sqlite3` file
