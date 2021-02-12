# celery
>[django x celery x redis setup](https://testdriven.io/blog/django-and-celery/)

## Task Queue
> 쓰레드나 머신에 작업을 분배하기 위해 쓰이는 장치

- distribute workloads

- celery는 *message* 를 통해 통신하고, 클라이언트와 worker를 연결하는 브로커(ex. redis)를 이용한다.
- 일 시작 -> 클라이언트: 큐에 message 전달 -> 브로커: 메세지 to worker

<br>

## Quick Cheat Sheet

- T.delay(arg, kwarg=value)
Star arguments shortcut to .apply_async. (.delay(*args, **kwargs) calls .apply_async(args, kwargs)).

- T.apply_async((arg,), {'kwarg': value})

- T.apply_async(countdown=10)
executes in 10 seconds from now.

- T.apply_async(eta=now + timedelta(seconds=10))
executes in 10 seconds from now, specified using eta

- T.apply_async(countdown=60, expires=120)
executes in one minute from now, but expires after 2 minutes.

- T.apply_async(expires=now + timedelta(days=2))
expires in 2 days, set using datetime.