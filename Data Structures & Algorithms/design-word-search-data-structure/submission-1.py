class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:

        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                newNode = TrieNode()
                curr.children[index] = newNode
            curr = curr.children[index]

        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        
        def dfs(node, i):
            if i == len(word):
                return node.isEndOfWord

            c = word[i]

            if c == ".":
                for child in node.children:
                    if child is not None and dfs(child, i + 1):
                        return True
                return False
            else:
                idx = ord(c) - ord('a')
                if node.children[idx] is None:
                    return False
                return dfs(node.children[idx], i + 1)

        return dfs(self.root, 0)


        
