# env files

## environment variables can be saved in a file
- pg-env.list
```
PG_MODE=primary
PG_PRIMARY_USER=postgres
PG_PRIMARY_PASSWORD=123456
PG_DATABASE=testdb
PG_USER=postgres
PG_PASSWORD=123456
PG_ROOT_PASSWORD=123456
PG_PRIMARY_PORT=5432
```
- to run `docker run --env-file=pg-env.list -------`