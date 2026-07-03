class Node:
    def __init__(self, ends: bool = False):
        self.hashmap = dict()
        self.ends = ends


class PrefixTree:
    def __init__(self):
        self.root = Node()

        

    def insert(self, word: str) -> None:
        cur = self.root

        for i in range(len(word)):
            c = word[i]
            
            if c not in cur.hashmap:
                if i == len(word) - 1:
                    cur.hashmap[c] = Node(True)
                else:
                    cur.hashmap[c] = Node()
            
            if i == len(word) - 1:
                cur.ends = True

            cur = cur.hashmap[c]


    def search(self, word: str) -> bool:
        cur = self.root

        for i in range(len(word)):
            c = word[i]

            if c not in cur.hashmap:
                return False
            
            if i == len(word) - 1:
                break

            cur = cur.hashmap[c]

        return cur.ends

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for i in range(len(prefix)):
            c = prefix[i]

            if c not in cur.hashmap:
                return False
            
            cur = cur.hashmap[c]
        
        return True




