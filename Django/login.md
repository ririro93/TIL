# login
> [coding entrepreneurs](https://github.com/codingforentrepreneurs/Django-Bootcamp-1)
## authenticate, login, logout
`from django.contrib.auth import authenticate, login, logout`
- 로그인하면 request.user이 계속 username이 저장되어있는거

ex).
```python
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST of None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('/')
        # if invalid
        else:
            ## 이런 식으로 많이 틀리면 다른데로 보내든가 할 수 있음
            # attempt = request.session.get('attempt', 0)
            # request.session['attempt'] = attempt + 1
            # return redirect('/invalid-password')
            request.session['invalid_user'] = 1
    return render(request, 'forms.html', {'form': form})
```

## user
in models.py
- `User = settings.AUTH_USER_MODEL`

in views.py
- `User = get_user_Model()`

<br>

## login with socials
[medium post](https://whizzoe.medium.com/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5)
- use django-allauth