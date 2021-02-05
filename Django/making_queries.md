# Making Queries

## Get certain values from Model
> list로 형변환 안 시켜주면 `Queryset` object로 반환돼서 쓰기 힘들다
```python
results = list(Model.objects.value())
results = list(Model.objects.value_list('id'))
results = list(Model.objects.value('id', flat=True))
```
1. `value()`는 key, value 쌍의 딕셔너리의 리스트 반환
2. `value_list()`는 (key, value)의 튜플 반환
3. `value_list(flat=True)`는 값만 들어간 리스트 반환


## Chaining filter, exclude
- filters and excludes can be chained like this to get objects within a certain period
- [CAUTION] : datetime objects seem to always include time so if you use `gt=today` to try to exclude objects from the day after, objects from today also get excluded because filters consider time as well not just the date.
  - using `today = datetime.datetime(year, month, day)` doesn't create just a date, it creates a date + time with 00:00 as the default time
  - to achieve this effect you should use `gt=today(23:59)` considering time or simply use `gte=the day after today`
```python
solves = Solve.objects.filter(
  member__member_id=self.member_id,
  solved_time__gte=start_date,
).exclude(
  solved_time__gte=end_date # actually the day after the last day you want to include
)
```