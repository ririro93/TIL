# postgres:12.0-alpine

## 사용법
도커에서 얘를 쓸려면 
- 프로젝트 폴더에서 `pip install psycopg2-binary` 써주고 근데 검색해보니까 엥?
    - [django](https://code.djangoproject.com/ticket/30483) Note: The psycopg2-binary package is meant for beginners to start playing with Python and PostgreSQL without the need to meet the build requirements.
If you are the maintainer of a publish package depending on psycopg2 you shouldn’t use ‘psycopg2-binary’ as a module dependency. For production use you are advised to use the source distribution.
Note: The binary packages come with their own versions of a few C libraries, among which libpq and libssl, which will be used regardless of other libraries available on the client: upgrading the system libraries will not upgrade the libraries used by psycopg2. Please build psycopg2 from source if you want to maintain binary upgradeability.
Warning: The psycopg2 wheel package comes packaged, among the others, with its own libssl binary. This may create conflicts with other extension modules binding with libssl as well, for instance with the Python ssl module: in some cases, under concurrency, the interaction between the two libraries may result in a segfault. In case of doubts you are advised to use a package built from source.
    - 얘 빼고 테스트 해보기 -> 없어도 됨
- Dockerfile에다가 밑 실행해줘야됨, python-alpine에 밑 requirements가 포함 안돼있어서
    ```
    RUN apk update \
        && apk add postgresql-dev gcc python3-dev musl-dev
    ```
