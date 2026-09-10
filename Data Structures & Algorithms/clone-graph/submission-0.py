"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        CloneNode = Node(node.val)
        node_dict = {node : CloneNode}

        queue = [node]

        while queue:
            cur = queue.pop()
            for neighNode in cur.neighbors:
                
                if neighNode in node_dict:
                    (node_dict[cur].neighbors).append(node_dict[neighNode])
                    continue
                
                queueNode = Node(neighNode.val)
                node_dict[neighNode] =  queueNode

                (node_dict[cur].neighbors).append(queueNode)
                queue.append(neighNode)
        
        return CloneNode
        