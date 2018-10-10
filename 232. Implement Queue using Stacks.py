#Stack
from collections import deque
class Stack:
    def __init__(self):
        self.date=deque()
    def push(self,e):
        self.date.append(e)
    def pop(self):
        if (len(self.date)>0):
            return self.date.pop()
        else:
            return None
    def peek(self):
        if(len(self.date)>0):
            return self.date[len(self.date)-1]
        else:
            return None
    def getSize(self):
        return len(self.date)
    def isEmpty(self):
        return len(self.date)==0
