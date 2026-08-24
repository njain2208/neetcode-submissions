# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next
        
        
        cur = head
        ans = tempStart = ListNode()
        
        for i in range(length//k):
            prev = ListNode()
            startNode = cur
            for j in range(k):
                temp = cur.next
                cur.next = prev

                prev = cur
                cur = temp

            tempStart.next = prev
            tempStart = startNode
        tempStart.next = cur

        return ans.next



