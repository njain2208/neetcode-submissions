# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        slowPtr = head
        fastPtr = head
        while fastPtr.next and fastPtr.next.next:
            if fastPtr.next.next ==  slowPtr:
                return True
            
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        return False
        