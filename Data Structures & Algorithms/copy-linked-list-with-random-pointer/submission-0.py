"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deepCopy = {}
        newHead = prev = Node(0)
        cur = head

        while cur:
            temp = Node(cur.val)
            prev.next = temp

            prev = temp
            deepCopy[cur] = temp

            cur = cur.next
        
        for key in deepCopy.keys():
            if key.random != None:
                deepCopy[key].random =  deepCopy[key.random]

        return newHead.next
