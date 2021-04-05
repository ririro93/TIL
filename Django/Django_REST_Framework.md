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