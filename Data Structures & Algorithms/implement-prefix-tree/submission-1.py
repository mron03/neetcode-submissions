class Node:
    def __init__(self):
        self.children = dict()
        self.ends = False


class PrefixTree:
    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            
            cur = cur.children[c]
        
        cur.ends = True


    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        return cur.ends

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        
        return True




