# 01-25 : [Leetcode] 21. Merge Two Sorted Lists

<details>
<summary>Problem</summary>
<p>
Merge two sorted linked lists and return it as a **sorted** list. The list should be made by splicing together the nodes of the first two lists.
![img](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

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



# My 1st solve

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

