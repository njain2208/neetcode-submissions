# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carryOver = 0
        ans = prev = ListNode()

        while l1 or l2:
            l1_val = l1.val if l1 != None else 0
            l2_val = l2.val if l2 != None else 0

            nodeSum = l1_val + l2_val + carryOver
            carryOver = nodeSum//10

            prev.next = ListNode(nodeSum%10)
            prev = prev.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carryOver != 0:
            prev.next = ListNode(carryOver)

        
        return ans.next