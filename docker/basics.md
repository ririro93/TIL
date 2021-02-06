# basics

## 도커가 뭐냐
[유튜브 playlist](https://www.youtube.com/watch?v=o6o5N4S5k84&list=PLOLrQ9Pn6cazCfL7v4CdaykNoWMQymM_C&index=3)
> 도커는 데이터베이스가 들어있는 컨테이너, 파이썬 컨테이너, redis 컨테이너 등을 생성, 관리해준다.

- 컨테이너는 소프트웨어가 설치되어 있는 독립적인 박스 
- 도커는 얘네가 서로 정보 주고 받을 수 있게 해주고
- containers are not OS specific
- build images -> run with docker -> run as containers
- image : container = class : instance 느낌

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
- shared across multiple running containers -> save resources



<br>

## 명령어
> [얄코-명령어 모음](https://www.yalco.kr/36_docker/) <br>

- `search <image-name>` : 검색 가능
- `run -t -i` : terminal, interactive(run in foreground not background) `-d`: background
- `container run -d -p 8080:80 --name apacheinstance httpd`: -p (=port) 8080:80(내 포트 8080, 컨테이너 포트 80)
- `images` : 내 컴에 저장된 도커 이미지들 목록 보여줌 <br>
- `image rm <image-name>` : remove image
- `ps` : (**p**rocess **s**tatus) 작업 진행중인 도커 컨데이너들 목록 <br>
  - -a 를 붙이면 작업 중지 중인 애들도 보임 <br>
- `exec -it <container-name> bash` : 해당 컨테이너 bash shell 실행 <br>
- `stop $(docke ps -aq)` : 모든 컨테이너 중지 <br>
- `container prune` : 컨테이너 다 삭제
- `container logs --tail 100 <container-name>` : 마지막 로그 100줄 
- `system prune-a` : 사용되지 않는 모든 도커 요소(컨테이너, 이미지, 네트워크, 볼륨 등) 삭제 <br> 
- `build -t <imge-name> .` : Dockerfile 파일이 있는 디렉토리 기준.  마지막의 . 이 상대주소
- `run -it --rm-p 6379:6379 "cfe-redis"`: 
- -it --rm is o this docker container only runs when we want it to and the container will be removed after we’re done runing it.
- -p 6379:6379is exposing the port 6379 on our local system AND in our docker container.
<br
## docker file
> 도커 파일은 도커 이미지를 만들기 위한 설계도

`RUN` : 이미지를 생성하는 과정에서 실행 <br>
`CMD` : 컨테이너 가동될 때 바로 실행 <br>
