# Django REST Framework

## serializers.py
- 장고 모델 데이터 -> 템플릿 -> 웹에 보여주기 (다 장고가 알아서 해줌)
- 하지만 다른데에선 모델 데이터를 이해할 수 없어서 통신을 하기 위해서는 JSON으로 바꿔줘야함(직렬화)
- 그래서 사용하는 것이 Serializer

## views.py
> `from rest_framework import viewsets`
- viewset이라는 cbv를 사용한다
- CRUD 로직이 다 구현되어 있는 view

## urls.py
```python
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

- 라우터를 사용해서 url 관리를 한다

## auth
> django-rest-auth [docs](https://django-rest-auth.readthedocs.io/en/latest/index.html)
uses Django's Token-based authentication
- django-rest-auth is heavily dependant on django-allauth
    - to change config -> change allauth config
        - ex). to change username field to required=False for signup
            - set `ACCOUNT_USERNAME_REQUIRED = False`

### problem
- tried using django token authentication with django-rest-auth but sessions were also created -> no point in using token authentication?
- -> if designed this way why use tokens in first place
- -> my settings are incorrect