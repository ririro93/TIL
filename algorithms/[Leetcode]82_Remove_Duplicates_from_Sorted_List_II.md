# 01-26 : [Leetcode]82_Remove_Duplicates_from_Sorted_List_II

> Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

### example1
```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

### example2
```
Input: head = [1,1,1,2,3]
Output: [2,3]
```

<details open>
<summary>1st 풀이: 노드 3개씩 보면서 중간값이 양옆값이랑 다르면 리스트에 추가</summary>

- linked list에 대한 이해도가 부족한 풀이였던거 같다
- `dummy.next = node1` 이라고 선언하면 자동으로 dummy.next.next는 node1.next 가 되고 뒤에 줄줄이 붙는다
- 위 같은 특성을 사용하면 새로운 linked list를 만들기 보단 그냥 next로 가리키는 노드만 바꾸면서 원하는 linked list를 얻을 수 있다 -> 2nd 풀이

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 애초에 없을 때
        if not head:
            return head
        
        # init
        dummy = tail = ListNode()
        prev = ListNode(101)
        curr = head.next
        
        # prev-head-curr 순으로 생각해서 head 가 prev랑도 다르고 curr랑도 다르면 추가
        while curr:
            if prev.val != head.val and head.val != curr.val:
                tail.next = head
                tail = head
            prev = head
            head = curr
            curr = head.next
        # 마지막에 두개 남았을 때 or 애초에 1개 밖에 없을 때
        if prev.val != head.val:
            tail.next = head
            tail = head
        tail.next = None # 이걸 해줘야지 뒤에 붙어있던 애들 자를수있다
        return dummy.next
```

</details>

<details open>
<summary> 2nd 풀이 : 중복은 건너뛰고 다음애를 .next로 가리키는 식으로 </summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # pre는 중복되는 부분 전에 마지막 애를 가리키도록
        dummy = pre = ListNode(0, head)
        dummy.next = head
        
        while head and head.next:
            # 중복 시작 부분
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pre.next = head.next
            # 새로운 노드 등장
            else:
                pre = pre.next
            head = head.next
        
        return dummy.next
```

</details>

# 배운 점
- linked list 감 좀 잡았다 -> .next 를 선언하면 노드 하나만 뒤에 붙는게 아니라 넝쿨째 통째로 붙는거다




