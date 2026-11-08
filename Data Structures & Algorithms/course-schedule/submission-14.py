class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)


        visited = set()

        def dfs(root):
            if root in visited:
                return True

            visited.add(root)
            for n in hashmap[root]:
                if dfs(n):
                    return True
            
            visited.remove(root)
            hashmap[root] = []
            return False
        

        for course in range(numCourses):
            if dfs(course):
                return False
        
        return True

