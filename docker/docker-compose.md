# docker-compose

## opening shell of service
execute shell of a docker-compose service <br>
`docker-compose exec <service-name> sh`

Bring down the development containers (and the associated volumes with the -v flag): <br>
`docker-compose down -v`

이런식으로 개발 때랑 배포 때랑 다른 docker-compose 파일을 써버리네 <br>
(여기다는 gunicorn 쓰고 개발 때는 그냥 django development server 쓰고) <br>
`docker-compose -f docker-compose.prod.yml up -d --build` <br>
--build flag는 먼저 이미지 build하고 컨테이너 말들어라 이말