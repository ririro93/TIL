# pgAdmin4

## run pgAdmin and postgresql with docker
[doc](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html)

1. 일단 환경변수 설정해둔 파일 2개 만든다 <br>

    `pg-env.list` 파일

    ```
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=postgres
    ```

    `pgadmin-env.list` 파일
    ```
    PGADMIN_DEFAULT_EMAIL=postgres@gmail.com
    PGADMIN_DEFAULT_PASSWORD=postgres
    ```

2. 각각 이미지에 환경변수 넣어서 도커로 실행시킨다 
    ```
    docker run -p 5432:5432 --env-file=pg-env.list -d --name pgdb postgres
    docker run -p 80:80 --env-file=pgadmin-env.list -d --name pgadmin dpage/pgadmin4
    ```

3. **ubuntu bash 하나 켜서 ifconfig로 wsl의 ip 주소 확인한다** (여기서 엄청 해맸다..)
    -> 얘가 그냥 docker-compose로 django, postgresql, pgadmin 다 묶어보리니깐 그냥 172.22.0.1 내부 네트워크?(subnet)으로도 잘 잡힌다ㅎㅎ..
4. localhost/80 들어가서 로그인하고 add server하면 됨
