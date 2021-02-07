# environment variables

프로그램 밖에 저장하기 위해 -> file system 에 저장되는게 아니라 os 내부에서 비밀스럽게 관리됨

make .env file and store environment variables in here <br>
use them by calling `os.getenv('<environment-variable-name>')`

ex). .env file <br>
**##주의##** : 변수명이랑 변수 사이에 띄어쓰기 하면 안됨!
```
# Django
SECRET_KEY='asfakshfklahsfkahewkfhak'
```

settings.py file
```python
SECRET_KEY = os.getenv('SECRET_KEY')
```

## env variables for django
[django-environ](https://django-environ.readthedocs.io/en/latest/)
```python
import environ

env = environ.Env()

# reading .env file
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
```