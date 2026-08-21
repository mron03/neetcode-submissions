class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapp = defaultdict(list)
        for edge in edges:
            mapp[edge[0]].append(edge[1])
            mapp[edge[1]].append(edge[0])
        
        print(mapp)
        res = 0
        visited = set()

        def dfs(i):
            visited.add(i)

            for edge in mapp[i]:
                if edge not in visited:
                    dfs(edge)


        for i in range(n):
            if i not in visited:
                dfs(i)    
                res += 1                

        return res
        
