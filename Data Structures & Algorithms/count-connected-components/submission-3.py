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
        for edge in edges:
            if edge[0] not in visited:
                dfs(edge[0])
                result += 1
        
        return result + n - len(visited)
            


        
