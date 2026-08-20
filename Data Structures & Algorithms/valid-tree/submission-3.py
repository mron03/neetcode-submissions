class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mapp = defaultdict(set)
        for edge in edges:
            mapp[edge[0]].add(edge[1])
            mapp[edge[1]].add(edge[0])

        visited = set()

        def dfs(c, p):
            if c in visited: return False

            visited.add(c)

            for edge in mapp[c]:
                if edge == p:
                    continue

                if not dfs(edge, c):
                    return False

            return True
        

        return dfs(0, -1) and len(visited) == n
            
