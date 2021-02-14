# celery-beat
> 얘는 celery를 언제 실행시킬지 알려주는 scheduler 인데 django에서는 django_celery_beat라는 애를 INSTALLED_APPS에 넣어서 쉽게 쓸 수 있다.

- (주의) : 멋도 모르고 settings.py에서 다른 app의 tasks.py를 임포트 했다가 거기서 에러가 나서 settings.py가 다 먹통이 돼서 앱 실행도 안되고 원인 찾는데 고생했다. 처음엔 SECRET_KEY must not be empty 이런 메세지 뜨길래 os.environ이 잘못된걸줄 알았는데 그 부분 코드가 읽히지도 않은거였다.

- 장고에서 celery-beat 실행
    - `$ celery -A proj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
