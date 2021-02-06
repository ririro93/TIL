# basics

## 명령어
> [얄코-명령어 모음](https://www.yalco.kr/36_docker/) <br>

`docker images` : 내 컴에 저장된 도커 이미지들 목록 보여줌 <br>
`docker ps` : (**p**rocess **s**tatus) 작업 진행중인 도커 컨데이너들 목록 <br>
  - -a 를 붙이면 작업 중지 중인 애들도 보임 <br>

`docker exec -it <container-name> bash` : 해당 컨테이너 bash shell 실행 <br>
`docker stop $(docker ps -aq)` : 모든 컨테이너 중지 <br>
`docker system prune -a` : 사용되지 않는 모든 도커 요소(컨테이너, 이미지, 네트워크, 볼륨 등) 삭제 <br> 
`docker build -t <image-name> .` : Dockerfile 파일이 있는 디렉토리 기준.  마지막의 . 이 상대주소

<br>

## what is a docker image?
> 도커의 이미지란 리눅스 컴퓨터의 특정 상태를 캡쳐해서 박제해 놓은 것을 말함.

`docker run -it node`를 실행하면 <br>
먼저 내 컴퓨터에서 `node`라는 이미지를 찾아보고 없으면 도커 허브에서 다운 받아주고 <br>
-> 내 컴퓨터에서 컨테이너 만들어준다 <br>
-> `-it`: 컨테이너 생성 후 그 CLI 사용하겠다 <br>
-> 이 이미지의 경우 바로 node까지 실행하도록 설계가 되어있네

[참고 블로그](https://www.44bits.io/ko/post/why-should-i-use-docker-container#%EC%84%9C%EB%B2%84%EB%A5%BC-%EC%BD%94%EB%93%9C%EB%A1%9C-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B3%A0-%EA%B4%80%EB%A6%AC%ED%95%98%EB%8A%94-%EB%8B%A4%EC%96%91%ED%95%9C-%EB%B0%A9%EB%B2%95)


[참고 유튜브](https://www.youtube.com/watch?v=hWPv9LMlme8&t=8s)

<br>

## docker file
> 도커 파일은 도커 이미지를 만들기 위한 설계도

`RUN` : 이미지를 생성하는 과정에서 실행 <br>
`CMD` : 컨테이너 가동될 때 바로 실행 <br>
