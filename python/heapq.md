# Heapq

### data structure : heap

- 리스트에서 가장 작거나 가장 큰 수를 pop 할 때 씀
- `heapq.heappush(<list>, ele)` 랑 `heapq.heappop(<list>, ele)` 둘다 O(logn) time complexity



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