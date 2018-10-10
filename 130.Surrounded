class Solution:
    class UnionFind:
        class Node:
            def __init__(self,x,y,root):
                self.x,self.y,self.root=x,y,root

        def __init__(self,maxX,maxY):
            self.maxX,self.maxY,self.data,self.noChange = maxX,maxY,list(),set()
            self.board = [[None for j in range(maxY)] for i in range(maxX)]
        
        #添加节点
        def add(self,x,y):
            node = self.Node(x,y,len(self.data))
            self.data.append(node)
            self.board[x][y] = node
            
            if node.x==0 or node.y==0 or node.x==self.maxX-1 or node.y==self.maxY-1:
                self.noChange.add(node)
            self.setRoot(x,y,node)
        #
        def setRoot(self,x,y,node):
            self.setNeigNode(x-1,y,node)
            self.setNeigNode(x+1,y,node)
            self.setNeigNode(x,y-1,node)
            self.setNeigNode(x,y+1,node)
            
        def setNeigNode(self,x,y,node):
            if x<0 or x>=self.maxX or y<0 or y>=self.maxY: return 
            if self.board[x][y] != None:
                neigRoot = self.find(self.board[x][y].root)
                if self.data[neigRoot] in self.noChange:
                    node.root = neigRoot
                else:
                    self.data[neigRoot].root = node.root
        
        #获得需要修改的节点
        def getNeedChange(self):
            ret = list()
            for i in self.data:
                if self.data[self.find(i.root)] not in self.noChange:
                    print(i.x,i.y)
                    ret.append(i)
            return ret
                
        #找到根节点
        def find(self,index):
            while self.data[index].root != index:
                self.data[index].root = self.data[self.data[index].root].root
                index = self.data[index].root
            return index
                
                
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) <= 0 or len(board[0]) <=0 :return
        maxX,maxY= len(board),len(board[0])
        uf = self.UnionFind(maxX,maxY)
        for x in range(maxX):
            for y in range(maxY):
                if board[x][y] == 'O':
                    uf.add(x,y)
        neetChange = uf.getNeedChange();
        for i in neetChange:
            x,y = i.x,i.y
            board[x][y] = 'X'
        
        
        
