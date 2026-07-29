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

        sett = {}

        def bfs(cur):
            if cur.val in sett:
                return

            cur_copy = Node(val=cur.val)
            sett[cur.val] = cur_copy
            neighbors_copy = []

            for n in cur.neighbors:

                if n.val in sett:
                    neighbor_copy = sett[n.val]
                else:
                    neighbor_copy = bfs(n)

                neighbors_copy.append(neighbor_copy)

            cur_copy.neighbors = neighbors_copy
            
            return cur_copy

        return bfs(node)


            


            