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