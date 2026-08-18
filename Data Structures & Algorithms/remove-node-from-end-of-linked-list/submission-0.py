# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linkedListLen = 0

        cur = head

        while cur:
            linkedListLen += 1
            cur = cur.next
        
        nthNode = linkedListLen - n+1

        prev = ListNode()
        startNode = prev
        prev.next = head

        cur, i  = head, 0

        while cur:
            i += 1
            if i == nthNode:
                temp = cur
                prev.next = cur.next

                cur.next = None
                del cur
                break


            prev = cur
            cur = cur.next
        return startNode.next

        