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

        def dfs(word, root):
            for i in range(len(word)):
                if word[i] != ".":
                    if word[i] in root.children:
                        root = root.children[word[i]]
                        continue
                    else:
                        return False

                
                for k, v in root.children.items():
                    res = dfs(word[i+1:], v)
                    if res:
                        return True

                return False
                
            return root.ends


        return dfs(word, self.root)



class WordDictionary:

    def __init__(self):
        self.tree = PrefixTree()
        

    def addWord(self, word: str) -> None:
        self.tree.insert(word)
        

    def search(self, word: str) -> bool:
        return self.tree.search(word)

        
