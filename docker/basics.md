# basics

## 도커가 뭐냐
[유튜브 playlist](https://www.youtube.com/watch?v=o6o5N4S5k84&list=PLOLrQ9Pn6cazCfL7v4CdaykNoWMQymM_C&index=3)
> 도커는 데이터베이스가 들어있는 컨테이너, 파이썬 컨테이너, redis 컨테이너 등을 생성, 관리해준다.

<br>

## docker container
- 컨테이너는 소프트웨어가 설치되어 있는 독립적인 박스 
- 도커는 얘네가 서로 정보 주고 받을 수 있게 해주고
- containers are not OS specific
- build images -> run with docker -> run as containers
- image : container = class : instance 느낌
- ubuntu 같은애는 running process 가 없어서 만들자 마자 exit 되는거 -> 뭔가 실행되고 있어야지 container가 켜져 있는다

<br>

## docker image
> 도커의 이미지란 리눅스 컴퓨터의 특정 상태를 캡쳐해서 박제해 놓은 것을 말함.

> a group of layers
- a collection of filesystem layers and metadata
- can be executed to create containers
- container가 있으면 이미지 지울 수 없음

`docker run -it node`를 실행하면 <br>
먼저 내 컴퓨터에서 `node`라는 이미지를 찾아보고 없으면 도커 허브에서 다운 받아주고 <br>
-> 내 컴퓨터에서 컨테이너 만들어준다 <br>
-> `-it`: 컨테이너 생성 후 그 CLI 사용하겠다 <br>
-> 이 이미지의 경우 바로 node까지 실행하도록 설계가 되어있네

[참고 블로그](https://www.44bits.io/ko/post/why-should-i-use-docker-container#%EC%84%9C%EB%B2%84%EB%A5%BC-%EC%BD%94%EB%93%9C%EB%A1%9C-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B3%A0-%EA%B4%80%EB%A6%AC%ED%95%98%EB%8A%94-%EB%8B%A4%EC%96%91%ED%95%9C-%EB%B0%A9%EB%B2%95)


[참고 유튜브](https://www.youtube.com/watch?v=hWPv9LMlme8&t=8s)

<br>

## docker layer
- shared across multiple running containers -> save resources, faster builds
- ex). example layered architecture
  - layer1 : ubuntu
  - layer2 : apt package
  - layer3 : source code
  - layer4 : entrypoint
  - ======================== image (read only)
  - layer5 : container layer
  - ======================== container (read write)

<br>

## docker volume
> 내가 만든 컨테이너에 있는 db의 데이터를 저장하고 싶으면?

- 컨테이너를 만들 때 volume 을 mount 하면서 만든다 **Volume mounting**
- `docker volume create data_volume` 
- -> `docker run -v data_volume:/var/lib/mysql mysql`
- -> 이름 없는 volume을 mount 하려 하면 새로 생성해준다
- **bind mount**:
- -> `docker run -v /data/--- :/var/lib/mysql mysql` : 이렇게 경로 지정해서 이미 있는 dir를 연결 시킨다
- -> `--mount type=bind, source=/, target=/` : 이렇게도 실행 가능




<br>

## 명령어
> [얄코-명령어 모음](https://www.yalco.kr/36_docker/) <br>

- `search <image-name>` : 검색 가능
- `run -t -i` : terminal, interactive(run in foreground not background) `-d`: (detached) background
- `container run -d -p 8080:80 --name apacheinstance httpd`: -p (=port) 8080:80(내 포트 8080, 컨테이너 포트 80)
- `images` : 내 컴에 저장된 도커 이미지들 목록 보여줌 
- `image rm <image-name>` : remove image
  - `rmi <image-name>` : 얘도 같은 결과
- `ps` : (**p**rocess **s**tatus) 작업 진행중인 도커 컨데이너들 목록 
  - -a 를 붙이면 작업 중지 중인 애들도 보임 
- `exec -it <container-name> bash` : 해당 컨테이너 bash shell 실행 
- `stop $(docke ps -aq)` : 모든 컨테이너 중지 
- `container prune` : 컨테이너 다 삭제
- `inspenct <container-name>` : 더 자세한 내용 조회
- `image prune` : 이미지 다 삭제
- `container logs --tail 100 <container-name>` : 마지막 로그 100줄 
- `system prune -a` : 사용되지 않는 모든 도커 요소(컨테이너, 이미지, 네트워크, 볼륨 등) 삭제 
- `build -t <image-name> .` : Dockerfile 파일이 있는 디렉토리 기준.  마지막의 . 이 상대주소, -t(tag)
- `run -it --rm-p 6379:6379 "cfe-redis"`: 
- `-it --rm` this docker container only runs when we want it to and the container will be removed after we’re done runing it.
- `-p 6379:6379` : expose the port 6379 on our local system AND in our docker container.

### ENV variables
- `docker run -e APP_COLOR=blue simple-webapp-color` : APP_COLOR이라는 환경변수를 blue로 넣어주겠다는 뜻
- `inspect`로 이 컨테이너에 어떤 ENV variable이 적용되었는지 볼 수 있다.

<br>

## docker file
> 도커 파일은 도커 이미지를 만들기 위한 설계도

- 혹시 에러가 나거나 내용이 추가 되어도 캐쉬에 각 명령에 대한 layer이 저장되어있어서 더 빨리 빌드 가능

`FROM` : base image(OS or an image that contains an OS)
`RUN` : 이미지를 생성하는 과정에서 실행 <br>
`COPY` : 내 로컬에 있는 파일(source code)들을 이미지에 넣는다
`CMD` : 컨테이너 가동될 때 바로 실행 <br>
`ENV PYTHONUNVEFFERED=1` : 파이썬 결과물 버퍼가 아니라 바로 터미널로 보이게
`RUN pip install -r requirements.txt` : `-r` 얘는 뒤에 있는 requirements 파일에 있는 애들 다 깔아라 라는 뜻
`ENTRYPOINT`["sleep"]` : 이건 컨테이너 실행시킬때 docker run ubuntu-sleeper 10 이라고 하면 되지만
  - `CMD sleep 5` 였다면 docker run ubuntu-sleeper **sleep** 10 이라고 했어댜 될거
  - `CMD` 는 완전히 덮어씌워짐 -> `ENTRYPOINT`는 뒤에 parameter가 추가됨
  - `ENTRYPOINT["sleep"] CMD["5"]` : 이렇게 둘다 쓰면 디폴트로 5가 들어가네
  - `--entrypoint sleep2.0` 라고 실행시키면 오버라이드 가능

<br>

## docker-compose
> used to build muliple containers at the same time
```
version: "3.8"               # docker-compose 버전

services: 
    django:
        build: .          # django라는 애를 지금 dir에 있는 Dockerfile 을 갖고 만들겠다
        container_name: django
        command: python manage.py runserver 0.0.0.0:8000
        volumes:
            - .:/usr/src/app  # 지금 내 폴더랑 컨테이너의 /usr/src/app을 연결시키겠다(동기화 느낌?)
        ports:
            - "8000:8000"     # 지금 내 포트 8000이랑 컨테이너 포트 8000이랑 연결한다
        depends_on:
            - pgdb
    pgdb:
        image: postgres
        container_name: pgdb
        environment:
            - POSTGRES_DB=postgres
            - POSTGRES_USER=postgres
            - POSTGRES_PASSWORD=postgres
```
docker-compose 없어도 가능은 하다 <br>
redis랑 frontend를 연결하고 싶으면 <br>
`docker run -d --name=vote -p 5000:80 --link redis:redis voting-app` 이런식으로 --link를 써주면 됨
-> 이거 docker-compose version1 -> 지금은 알아서 이름으로 통신하게 bridge network를 형성해준다

`image : ` 를 쓰면 이미 있는 이미지 갖다 쓰겠다는 뜻 <br>
`build : ` 를 쓰면 Dockerfile 이 있는 주소를 주면 거기 있는거 빌드해서 그 이미지 쓰라는 거 <br>
`depends_on: ` 을 쓰면 어떤 거를 먼저 만들어줘야된다고 알려주는거

<br>

