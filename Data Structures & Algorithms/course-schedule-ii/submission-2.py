class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = defaultdict(list)
        for prereq in prerequisites:
            premap[prereq[0]].append(prereq[1])

        visiting = set()
        visited = set()

        order = []

        def dfs(i):
            if i in visiting: return False  # cycle
            if i in visited: return True
            visiting.add(i)
            for prereq in premap[i]:
                if not dfs(prereq):
                    return False
            visiting.remove(i)
            visited.add(i)
            order.append(i)  # append AFTER prereqs are done
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order

    