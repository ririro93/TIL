# Linked List

## 문제 유형
- [[Leetcode] 21](https://github.com/ririro93/algorithm_probs/blob/master/leetcode/daily_problems/21_Merge_Two_Sorted_Lists.md) : 두 리스트를 합치는데 오름차순으로 되게 **합치기**

- [[Leetcode] 82](https://github.com/ririro93/algorithm_probs/blob/master/leetcode/daily_problems/82_Remove_Duplicates_from_Sorted_List_II.md) : 중복되는 원소 **제거**하기

## 배운 점
- 새로운 linked list를 생성할 때는 시작노드인 dummy node와 끝 노드인 tail node 를 미리 생성해두고 진행하면 편하다.
- in-place algorithm : 인풋 이외의 새로운 메모리를 필요로 하지 않는 코드
  ex). reversing an array
    ```python
    def reverseArray(arr, n):
        for i in range(0, int(n/2)):
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        return arr
    ```
- linked list 감 좀 잡았다 -> .next 를 선언하면 노드 하나만 뒤에 붙는게 아니라 넝쿨째 통째로 붙는거다

    
