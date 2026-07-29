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

        dic = {}

        def dfs(cur):
            cur_copy = Node(val=cur.val)
            dic[cur.val] = cur_copy
            
            for n in cur.neighbors:
                cur_copy.neighbors.append(dic[n.val] if n.val in dic else dfs(n))
            
            return cur_copy

        return dfs(node)


            


            