# Authentication

## Custom User
[blog](https://testdriven.io/blog/django-custom-user-model/)

1. add to settings `AUTH_USER_MODEL = 'accounts.CustomUser'`
2. make `manager.py` for creating users and superusers
3. set `USERNAME_FIELD = 'email'` for CustomUser in `models.py`

## allauth
[docs](https://django-allauth.readthedocs.io/en/latest/index.html)