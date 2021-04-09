# Django REST Framework

## serializers.py
- 장고 모델 데이터 -> 템플릿 -> 웹에 보여주기 (다 장고가 알아서 해줌)
- 하지만 다른데에선 모델 데이터를 이해할 수 없어서 통신을 하기 위해서는 JSON으로 바꿔줘야함(직렬화)
- 그래서 사용하는 것이 Serializer
- **serializing**: django model instance -> python nateive datatype -> json
- **deserializing**: vice-versa

- `serializer = SnippetSerializer(Snippet.objects.all(), many=True)`
    - -> `many=True` to serialize a queryset not just a single instance
- serializer model에 어떤 인자를 넣어주고 싶을 때 쓸 수 있는 방법
    - `__init__` method 에서 Meta 클래스를 참조하면서 fields를 가져오기 때문에 
    ```python
    class ChoiceSerializer(serializers.ModelSerializer):
        author = serializers.StringRelatedField()
        question = serializers.StringRelatedField()
        answers = serializers.StringRelatedField(many=True)

        class Meta:
            model = Choice
            fields = ('id', 'author', 'question', 'content', 'created_at', 'answers')

        def __init__(self, *args, **kwargs):
            self.answer = kwargs.get('answer', True)
            if not self.answer:
                kwargs.pop('answer')
            super().__init__(*args, **kwargs)
            if not self.answer:
                del self.fields['answers']
    ```
- read_only 속성
    - True로 설정해주면 post request를 보낼 때 required field가 아니게 된다.
```python
class ChoiceSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
```

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

- viewset인 경우 라우터를 사용해서 url 관리를 한다

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

<br>

## Viewset
>[velog](https://velog.io/@sjp5554/Django-Rest-Framework-33)

ViewSets are powerful, but...
Sometimes combining concrete API View with ViewSets can result in more flexible and robust API. For example, Profile model has avatar ImageField declared.

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username
```

Instead of updating avatar along with other Profile fields in one ViewSet, create another separate endpoint with `AvatarUpdateView(generics.UpdateAPIView)`.

```python
class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object
```

### @action decorator
> used to extend ModelViewSets to have more urls [docs](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/)
- `url_path` argument can be used in the decorator if url other than the method name is wanted
