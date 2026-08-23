# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge2Lists(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = cur = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next

                cur = cur.next
                cur.next = None
            else:
                cur.next = list2
                list2 = list2.next

                cur = cur.next
                cur.next = None

        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return head.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        while len(lists) > 1:
            tempList = []
            for i in range(0,len(lists)-1,2):
                tempList.append(self.merge2Lists(lists[i],lists[i+1]))
            
            if len(lists)%2 == 1:
                tempList.append(lists[-1])
            lists = tempList
        return lists[0] if lists else None
                

        