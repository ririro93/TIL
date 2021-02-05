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