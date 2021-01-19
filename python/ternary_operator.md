# Ternary Operator

- 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 활용된다
  - 아래와 같은 경우는 `value = ` 다음 부분이 ternary operator 인 것.

```python
num = int(input('숫자를 입력하세요 : '))
value = num if num >= 0 else -num
print(value)
```

