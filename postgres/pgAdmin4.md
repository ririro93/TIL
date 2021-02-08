# pgAdmin4

## run pgAdmin with docker
[doc](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html)
1. `docker pull dpage/pgadmin4` : pull image
2. `docker run -p 8089:80 -e PGADMIN_DEFAULT_EMAIL=<email address> -e PGADMIN_DEFAULT_PASSWORD=<password> -d dpage/pgadmin4`
3. 얘 실행시킬 때 넣어주는 ip주소는 windows 주소가 아니라 내 wsl ip 주소다..
    - ubuntu 켜서 ifconfig 치면 나옴