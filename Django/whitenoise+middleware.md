# middleware
> this is where **whitenoise** should be included to serve static files easily for production.
- middleware is executed before views after receiving requests
- and when my response object is served it is served after running all the middleware codes.

## whitenoise
[whitenoise docs](http://whitenoise.evans.io/en/stable/django.html)

### 1
```python
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  # ...
]
```

<br>


### 2
- nostatic option to use white noise even during dev -> to ensure dev, prod is always same
```python
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    # ...
]
```

<br>

### 3
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### 4
```
python manage.py collectstatic
```
-> this puts all the static files in the project to dir 'staticfiles'