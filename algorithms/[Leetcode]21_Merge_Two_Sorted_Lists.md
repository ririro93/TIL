# 01-25 : [Leetcode] 21. Merge Two Sorted Lists

<details open>
<summary>문제</summary>
<p>
Merge two sorted linked lists and return it as a **sorted** list. The list should be made by splicing together the nodes of the first two lists.

**Example 1:**

```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**

```
Input: l1 = [], l2 = []
Output: []
```

**Example 3:**

```
Input: l1 = [], l2 = [0]
Output: [0]
```

**Constraints:**
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `l1` and `l2` are sorted in **non-decreasing** order.
</p>
</details>



<details>
<summary>1st solve</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if either has no nodes
        if not l1:
            return l2
        if not l2:
            return l1
        
        # if both has nodes
        result = []
        a = l1
        b = l2
        
        while a and b:
            if a.val < b.val:
                result.append(a)
                a = a.next
            else:
                result.append(b)
                b = b.next
        while a:
            result.append(a)
            a = a.next
        while b:
            result.append(b)
            b = b.next

        # 여기 이렇게 두개나 먼저 빼는거 보다 좋은 방법 있을거 같은데 잘 모르겠다..
        start = result[0]
        curr = result[1]
        start.next = curr
        for node in result[2:]:
            curr.next = node
            curr = node
        return start
```
</details/>

<details>
<summary>2nd solve</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dummy to point to head and tail to point to last node
        dummy = tail = ListNode()
        
        # continue until one is empty
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        # if either ended or was empty from beginning 
        tail.next = l1 or l2
        return dummy.next  
```
</details/>

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
    
