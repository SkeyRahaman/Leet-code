from sortedcontainers import SortedList
from collections import deque
class SortedListWithSum:
    
    def __init__(self):
        self.mem = SortedList()
        self.summ = 0
        
    def add(self, num):
        self.mem.add(num)
        self.summ += num
        
    def remove(self, num):
        self.mem.remove(num)
        self.summ -= num




class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        
        self.dq = deque()
        self.left = SortedListWithSum()
        self.mid = SortedListWithSum()
        self.right = SortedListWithSum()
        

    def addElement(self, num: int) -> None:
        self.dq.append(num)
        #add to lists
        if len(self.dq) > self.m:
            r = self.dq.popleft()
            if r in self.right.mem:
                self.right.remove(r)
            elif r in self.mid.mem:
                self.mid.remove(r)
                x = self.right.mem[0]
                self.mid.add(x)
                self.right.remove(x)
            else:
                self.left.remove(r)
                
                x = self.right.mem[0]
                self.mid.add(x)
                self.right.remove(x)
                
                x = self.mid.mem[0]
                self.mid.remove(x)
                self.left.add(x)
        self.left.add(num)
        if len(self.left.mem) > self.k:
            b = self.left.mem[-1]
            self.left.remove(b)
            self.mid.add(b)
            
            if len(self.mid.mem) > (self.m-self.k-self.k):
                x = self.mid.mem[-1]
                self.mid.remove(x)
                self.right.add(x)
                
                
            
        #remove from lists

        
    def calculateMKAverage(self) -> int:
        # print(self.mid.summ/(self.m-self.k-self.k))
        return floor(self.mid.summ/(self.m-self.k-self.k)) if len(self.dq) >= self.m else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()