# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            if temp:
                prev = slow
                slow = temp
                
            else:
                break

        l1, l2 = head, slow
        while l1 and l2:
            temp, temp1 = l1.next, l2.next

            l1.next = l2
            l2.next = temp
            
            l1 = temp
            l2 = temp1
        
        if l1:
            print(l1.val)
            


            
            

            

        