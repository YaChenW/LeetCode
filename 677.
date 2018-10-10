class MapSum:
    class Node:
        def __init__(self,val=0):
            self.isWord = False
            self.next = dict()
            self.val=val
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if type(key) is not str or val == None: return
        cur = self.root
        for i in key:
            if  i not in cur.next:
                cur.next[i] = self.Node()
            cur = cur.next[i]
        cur.isWord = True
        cur.val = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        if type(prefix) is not str:return 0
        cur = self.root
        for i in prefix:
            if i not in cur.next:return 0
            cur = cur.next[i]
        return self.getSum(cur)
            
    def getSum(self,root):
        ret = root.val
        for i in root.next: ret+=self.getSum(root.next[i])
        return ret
            

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
