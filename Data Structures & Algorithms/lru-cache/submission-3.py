class Node():
    def __init__(self,key=-1, val = 0, prev=None, next = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.n = 0
        self.cacheMap = {}

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev =self.left

    def get(self, key: int) -> int:
        if key not in self.cacheMap:
            return -1

        if self.cacheMap[key].next != self.right:
            temp = self.cacheMap[key].next
            prevTemp = self.cacheMap[key].prev

            prevTemp.next = temp
            temp.prev = prevTemp

            self.cacheMap[key].next = self.right
            self.cacheMap[key].prev = self.right.prev

            self.right.prev.next = self.cacheMap[key]

            self.right.prev = self.cacheMap[key]

        return self.cacheMap[key].val

        

    def put(self, key: int, value: int) -> None:
        if key not in self.cacheMap and self.n == self.capacity:
            delNode = self.left.next
            self.left.next = delNode.next
            delNode.next.prev = self.left
            self.n -= 1

            delNode.next = None
            delNode.prev = None

            del self.cacheMap[delNode.key]
            del delNode
            

        

        if key not in self.cacheMap:
            self.n+=1
            newNode = Node(key,value, None, None)
        else:
            self.cacheMap[key].val  = value
            self.cacheMap[key].prev.next = self.cacheMap[key].next
            self.cacheMap[key].next.prev = self.cacheMap[key].prev

            self.cacheMap[key].prev = None
            self.cacheMap[key].next = None

            newNode = self.cacheMap[key]

        self.cacheMap[key] = newNode
        

        temp = self.right.prev
        temp.next = newNode
        newNode.prev = temp

        newNode.next = self.right
        self.right.prev = newNode



        






        
