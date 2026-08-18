class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(set)
        for prereq in prerequisites:
            premap[prereq[0]].add(prereq[1])
        
        visited = set()

        def dfs(i):
            if i in visited:
                return False

            if not premap[i]:
                return True

            visited.add(i)

            while premap[i]:
                prereq = premap[i].pop()
                if not dfs(prereq):
                    return False
            
            visited.remove(i)
            
            return True

        for i in range(numCourses):
            if i in premap and not dfs(i):
                return False
        
        return True