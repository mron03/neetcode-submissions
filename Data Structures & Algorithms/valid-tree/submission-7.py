class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
            
        hashmap = defaultdict(set)

        for pair in edges:
            hashmap[pair[0]].add(pair[1])
            hashmap[pair[1]].add(pair[0])

        visited = set()

        def is_cycle(parent, current):
            if current in visited:
                return True

            visited.add(current)

            for neighbor in hashmap[current]:
                if neighbor != parent and is_cycle(current, neighbor):
                    return True
            
            return False
                    
        answer = is_cycle(-1, edges[0][0])

        if len(visited) != n:
            return False
        
        return not answer
