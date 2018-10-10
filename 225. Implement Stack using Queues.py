#Queue
from collections import deque
class Queue:
    def __init__(self):
        self.date=deque()
    def enqueue(self,e):
        self.date.append(e)
    def dequeue(self):
        if (len(self.date)>0):
            return self.date.popleft()
        else:
            return None
    def getFront(self):
        if(len(self.date)>0):
            return self.date[0]
        else:
            return None
    def getSize(self):
        return len(self.date)
    def isEmpty(self):
        return len(self.date)==0