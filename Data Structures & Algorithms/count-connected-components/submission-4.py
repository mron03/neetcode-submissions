class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = defaultdict(set)

        for edge in edges:
            hashmap[edge[0]].add(edge[1])
            hashmap[edge[1]].add(edge[0])


        visited = set()

        def dfs(root):
            if root in visited:
                return

            visited.add(root)

            for neighbor in hashmap[root]:
                if neighbor not in visited:
                    dfs(neighbor)

        result = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                result += 1
        
        return result
            


        
