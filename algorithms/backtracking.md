# Backtracking

## 느낌

- 어떤 노드가 유망하지 않으면 부모 노드로 되돌아간 후 다른 자손노드를 검색 -> 시간 단축

- DFS 처럼 스택 사용

  

## 예시

### 4-Queens Problem

4 X 4 체스판에 서로 위협하지 않도록 4개의 퀸을 위치 시키는 문제

![image-20210124202331380](C:\Users\anuj\AppData\Roaming\Typora\typora-user-images\image-20210124202331380.png)

![image-20210124202627708](C:\Users\anuj\AppData\Roaming\Typora\typora-user-images\image-20210124202627708.png)

[참고 블로그](https://idea-sketch.tistory.com/)

DFS라면 (2,1), (2,2) 도 스택에 바로 넣어버리지만, 백트래킹에선 애초에 넣지 않는다



## 키포인트

- DFS와 다르게 스택에 넣기 전에 유망성을 확인해본다
- 유망하지 않으면 바로 배제하고 스택의 다음 노드를 확인해본다





