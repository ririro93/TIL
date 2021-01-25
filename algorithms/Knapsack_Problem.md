# Knapsack Problem

> K무게를 견딜 수 있는 가방에 N개의 물건을 집어넣는 문제

각 물건은 무게W 와 가치V를 갖는데 가방에 최대가치를 내는 조합으로 물건을 담기

<details>
<summary>1st 풀이</summary>

- 모든 물건들에 대해 루프를 돌리는데 체크를 한 조합의 무게값들만 저장하는 checked를 만들어서 매번 여기 있는 요소들에만 다음 물품의 무게를 더해봤다
- 이러면 모든 물건들에 대해 무든 무게가 아닌 지나친 물품에 대해 고려한 무게들만 체크하면 되니까 시간이 줄어들줄 알았다
- 또 max_heap을 사용해서 큰 무게부터 갱신해 나가기 위해 (cache에서 충돌이 일어나지 않게) checked에 큰 무게부터 넣었는데
- 결론 : 백준pypy3 기준 384명중 384등으로 시간이 가장 길었다ㅎㅎ..

```python
from sys import stdin
from heapq import heappush, heappop

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, K = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(N)]

# function
def solve(K):
    checked = [-0]
    cache = [0] * (K+1)
    max_val = sum([val for _, val in infos])
    for info in infos:
        checklist = []
        nchecked = []
        l = len(checked)
        for _ in range(l):
            checklist.append(heappop(checked))
        for ele in checklist:
            tmp_val = cache[-ele] + info[1]
            tmp_weight = -ele + info[0]
            if tmp_weight <= K and tmp_val > cache[tmp_weight]:
                if tmp_val == max_val:
                    return tmp_val
                cache[tmp_weight] = tmp_val
                nchecked.append(tmp_weight)
        for nele in nchecked:
            heappush(checklist, -nele)
        checked = checklist[:]
        # print('\ncache: ', cache[:K+1])
        # print('checked: ', checked)
    return max(cache)

# exe
print(solve(K))
```
</details>

<details>
<summary>2nd 풀이</summary>

> 1차원 배열의 cache를 이용해 각 물품을 사용할지 말지 보면서 각 무게의 최대 가치값 갱신하기

- 확실히 코드도 간결해지고 직관적이고 2차원 배열을 쓰는거보다 메모리 덜 쓸듯 하다

```python
from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# 동적 계획법으로 다시 풀어보기
# 모든 물건은 넣거나 말거나 두가지 경우의 수 밖에 없다

# inputs
N, K = map(int, input().split())

# init
cache = [0] * (K+1)

## exe
# 각 물건을 넣거나 말 때 각 무게에 대해 최대 가치 값을 구한다
for _ in range(N):
    W, V = map(int, input().split())
    # 무게가 K 일때는 기존의 K일때의 최대 가치와 K- W 중 큰 값을 저장한다
    for i in range(K, W-1, -1):
        cache[i] = max(cache[i], cache[i-W] + V)
print(cache[-1])
```    
        
</details>

<details>
<summary>3rd 풀이</summary>

> 고수님 풀이 참고해서 따라해본 dictionary 사용한 풀이
- 빠르다
- 쉽다

```python
from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline 

# inputs
N, K = map(int, input().split())

# init -> 무게 0 일때 가능한 최대가치 0 으로 가방 초기화
bag = {0:0}

# exe
for _ in range(N):
    W, V = map(int, input().split())
    tmp = {}
    # 전에 고려해본 모든 무게들에 대해서만 새 물품 넣었을 때 가치 높아지나 확인
    for key, val in bag.items():
        nW = W + key
        nV = V + val
        if nW > K:
            continue
        tmp[nW] = max(bag.get(nW, 0), nV)
        # max_val = max(max_val, tmp[nW])
    # 충돌 일어나지 않게 tmp에 저장했다가 한번에 업데이트
    bag.update(tmp)
# print(max_val) 이렇게 해봤는데 이러면 모든 경우의 수에 다 비교를 하니깐 시간 더 오래 걸린다 -> 2024ms
print(max(bag.values())) # 이렇게 하면 다 업데이트 하고 마지막에 남은 것들만 비교하니까 더 빠름 -> 1496ms 
```

</details>

## 배운점
- 0-1 knapsack(물건을 통째로 넣거나 아예 빼거나) 문제는 1차원 배열로 풀면 간단하고 빠르다
- 딕셔너리를 사용해서 접근해본 무게들만 key로 저장하면서 그 무게들에 대해서만 루프를 돌리면 계산량을 줄일 수 있다
    
