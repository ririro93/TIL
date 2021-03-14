# queryset

## creating new objects
1. `create`
```python
p = Person.objects.create(first_name="Bruce", last_name="Springsteen")
```
2. `save`
```python 
p = Person(first_name="Bruce", last_name="Springsteen")
p.save(force_insert=True)
```

## turning querysets into json
```python
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Post


def posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")
```

## filtering
- `filter(id=id)` 이건 `filter(id__exact=id)` 랑 같음
- `filter(id__iexact=id)`라고 하면 대소문자 구분없이 다 찾아줌