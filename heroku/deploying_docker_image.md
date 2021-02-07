# deploying docker image to heroku
1. 도커랑 heroku 둘다 로그인 한거 확인하고
2. `heroku create` : 새 앱 생성
3. `heroku container:login` 도 해줘야됨
4. `heroku container:push web -a=<heroku-app-name>`
5. `heroku config:add ALLOWED_HOSTS=* -a <heroku-app-name>` : 이걸로 env var 더하기
6. `heroku config:get ALLOWED_HOSTS=* -a <heroku-app-name>` : 이걸로 env var 보기
7. `heroku container:release web -a <heroku-app-name>` : 이걸로 release하기