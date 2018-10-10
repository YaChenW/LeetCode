class WordDictionary:

    class Node:
        def __init__(self):
            self.isWord = False
            self.next = dict()
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()
        self.size = 0

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if type(word) is str:
            cur = self.root
            for i in word:
                if not i in cur.next:
                    cur.next[i] = self.Node()
                cur = cur.next[i]
            if not cur.isWord:
                cur.isWord = True
                self.size+=1

    def search(self, word,index=0,cur=-1):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if cur == -1:
            if not type(word) is str: return False
            cur = self.root
        if index == len(word) :return cur.isWord
        
        if word[index] == '.':
            for i in cur.next:
                if self.search( word,index+1,cur.next[i] ):
                    return True
            return False
        return self.search( word,index+1,cur.next[word[index]] ) if word[index] in cur.next else False
            
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
