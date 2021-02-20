# context_processors
> [blog](https://www.semicolonworld.com/question/53701/django-redirect-to-previous-page-after-login)

## context dictionaries that can be used in templates
ex). get current path so user can come back to same page after logging in

in TEMPLATES.OPTIONS as default

```python
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)
```

```html
<a href="{% url django.contrib.auth.views.login %}?next={{ request.path }}">Login</a>
```