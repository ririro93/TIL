# db

## using heroku's db
[coding entrepreneurs](https://www.codingforentrepreneurs.com/blog/deploy-django-on-docker-to-heroku-opencv)
[heroku docs](https://devcenter.heroku.com/articles/heroku-postgresql)


## querying heroku postgres
- `heroku pg:psql -a <app-name>` : postgres has to be installed and be in PATH

## using postgres add-on
```python
import dj_database_url

DATABASE_URL = os.environ.get('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)
```