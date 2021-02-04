# Making Queries

## get certain values from Model
> list로 형변환 안 시켜주면 `Queryset` object로 반환돼서 쓰기 힘들다
```python
results = list(Model.objects.value())
results = list(Model.objects.value_list('id'))
results = list(Model.objects.value('id', flat=True))
```
1. `value()`는 key, value 쌍의 딕셔너리의 리스트 반환
2. `value_list()`는 (key, value)의 튜플 반환
3. `value_list(flat=True)`는 값만 들어간 리스트 반환
