# Heapq

### data structure : heap

- 리스트에서 가장 작거나 가장 큰 수를 pop 할 때 씀
- `heapq.heappush(<list>, ele)` 랑 `heapq.heappop(<list>, ele)` 둘다 O(logn) time complexity
- maxheap을 쓰고싶으면 각 element에 -1을 곱해서 heappush 하면 됨
  - heapppop 할 때 -1 곱해서 쓰면 됨



### usage example

```python
>> import heapq
>>> a = [2, 5, 3, 7, 6, 8]
>>> heapq.heappush(a, 4)
>>> a
[2, 5, 3, 7, 6, 8, 4]
>>> heapq.heappop(a)
2
>>> heapq.heappop(a)
3
>>> heapq.heappop(a)
4
```

### heapq with lists and tuples
- heappop pops them in ascending order
- but error occurs if both lists and tuples are mixed in

```python
from heapq import *

# just tuples (lists work the same way)
a = []
heappush(a, (1, 3, 3, 4))
heappush(a, (2, 2, 3))
heappush(a, (3, 2, 2))
heappush(a, (5, 5, 1))
heappush(a, (2, 3, 2))
heappush(a, (1, 3, 3))
for _ in range(6):
    print(heappop(a))

# output
'''
(1, 3, 3)
(1, 3, 3, 4)
(2, 2, 3)
(2, 3, 2)
(3, 2, 2)
(5, 5, 1)
'''

# lists and tuples
a = []
heappush(a, [1, 3, 3, 4])
heappush(a, [2, 2, 3])
heappush(a, (3, 2, 2))
heappush(a, [5, 5, 1])
heappush(a, (2, 3, 2))
heappush(a, [1, 3, 3])
for _ in range(6):
    print(heappop(a))

# output
'''
Traceback (most recent call last):
  File "1631_Path_With_Minimum_Effort.py", line 84, in <module>
    heappush(a, (3, 2, 2))
TypeError: '<' not supported between instances of 'tuple' and 'list'
'''
```
