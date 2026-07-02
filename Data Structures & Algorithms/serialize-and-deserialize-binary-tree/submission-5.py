# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""

        def dfs(root):
            nonlocal res
            if not root:
                res += "n,"
                return
            
            res = res + str(root.val) + ","

            dfs(root.left)
            dfs(root.right)
        dfs(root)

        return res
                
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")[:-1]
        print(data)
        def dfs(i):
            nonlocal data

            if i >= len(data) or data[i] == "n":
                return None, i
            
            node = TreeNode(data[i])
            
            node.left, i = dfs(i + 1)
            node.right, i  = dfs(i + 1)
            
            return node, i
   
        root, _ = dfs(0)
        return root
