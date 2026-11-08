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
            return 

        hashmap = {}

        def dfs(root):
            new_root = Node(root.val)

            hashmap[root] = new_root

            for n in root.neighbors:
                if n not in hashmap:
                    dfs(n)

        
        dfs(node)

        for old, new in hashmap.items():
            for n in old.neighbors:
                new.neighbors.append(hashmap[n])

        return hashmap[node]            
