# caching
[참고 사이트](https://shahriar.svbtle.com/Understanding-writethrough-writearound-and-writeback-caching-with-python)
> db까지 가지 않고 더 가까운 곳에서 데이터를 가져가서 더 빠르게 제공 할 수 있게 해주는 장치. <br>
ex). redis

그럼 모든 데이터를 cache에 저장하면 되자않나? 라고 생각한다면 큰 문제가 2가지 있는데. 
1. cache는 비싸다 보통 SSD를 쓴대. 
2. cache 에 데이터를 너무 많이 저장하면 결국 또 탐색이 오래 걸린다 -> cache 쓸 이유 없어짐

- 그래서 cache에 뭘 저장 하고 뭘 지우고 어떻게 저장하고 이런 전략들을 잘 설계해야된다. 이 설계 방식을 **cache policy** 라고 부른다.

- 흔히 쓰이는 **LRU(least recently used)** 는 큐처럼 가장 최근에 쓴 정보를 cache 맨 위에 저장하고 오래될수록 밑으로 밀어서 오래된 정보부터 삭제한다.
- **sliding window policy**라는 것도 있다는데 더 검색해보자.

<br>

## 기본적인 cache 데이터 저장 방식
1. write-through
    - cache와 db에  동시에 저장
    - 장점: cache 정보 날라가도 safe
    - 단점: 매번 두번씩 써야돼서 느림
    - 사용처: 조금 쓰고 많이 읽는 곳

2. write-around
    - db에만 저장
    - 장점: cache 범람 방지
    - 단점: 최근에 쓴 정보 cache에 없음
    - 사용처: 쓰고 자주 안 읽는 곳

3. write-back
    - 일단 cache에만 저장 -> 나중에 db에 알아서 저장
    - 장점: 빠름
    - 단점: 데이터 손실 가능성
    - 사용처: 읽기 쓰기 둘다 빨라서 셋 중 젤 빠르긴 하다

- 실제로는 섞어쓰고 다른 장치 추가해서 쓰고 더 다양하게 쓰인다고한다.

<br>

## Redis
> Remote Dictionary Server

- redis is a key-value store (but supports **complex datastructures**)
- No SQL db -> no tables, rows, cols
- **in-memery db** -> no writing to disk (although possible) -> *super fast*

### use cases
- optimization
- db
- leaderboard
- message broker
