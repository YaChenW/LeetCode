class Trie:
    class Node:
        def __init__(self,isWord=False):
            self.isWord = isWord
            self.next = dict()
    
    def __init__(self):
        self.root = self.Node()
        self.size = 0
    #添加单词
    def insert(self,word):
        if type(word) is str:
            cur = self.root
            for i in word:
                if not i in cur.next:
                    cur.next[i] = self.Node()
                cur = cur.next[i]
            if not cur.isWord:
                cur.isWord = True
                self.size+=1
    #是否包含单词
    def search(self,word):
        if type(word) is str:
            cur = self.root
            for i in word:
                if not i ißn cur.next:return False
                cur = cur.next[i]
            return cur.isWord
        return False
    def startsWith(self,prefix):
        if type(prefix) is str:
            cur = self.root
            for i in prefix:
                if not i in cur.next:return False
                cur = cur.next[i]
            return True
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
