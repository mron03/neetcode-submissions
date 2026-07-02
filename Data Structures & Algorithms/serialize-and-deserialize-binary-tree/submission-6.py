# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []

        def dfs(root):
            nonlocal vals
            
            if not root:
                vals.append("n")
                return
            
            vals.append(str(root.val))

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return ",".join(vals)
                
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = deque(data.split(","))

        def dfs():
            nonlocal vals

            val = vals.popleft()

            if val == "n":
                return None
            
            node = TreeNode(int(val))
            
            node.left = dfs()
            node.right  = dfs()
            
            return node
   
        return dfs()
