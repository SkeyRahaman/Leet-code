from sortedcontainers import SortedList
from collections import defaultdict
class MyCalendarThree:

    def __init__(self):
        self.mem = defaultdict(SortedList)
        self.mem1 = {}
        self.l = SortedList()
    
    def addd(self, level, start, end):
        print(level,start, end)
        output = level
        b = self.mem[level].bisect_right([start,end])
        if 0<=b-1<len(self.mem[level]):
            if start < self.mem[level][b-1][1]:
                output = self.add(level+1,start,self.mem[level][b-1][1])
                start = self.mem[level][b-1][1]
                
        if 0<=b<len(self.mem[level]):
            if end > self.mem[level][b][0]:
                output = max(output, self.add(level+1,self.mem[level][b][0],end))
                end = self.mem[level][b][0]
        self.mem[level].add([start,end])
        return output
                
        
        

    def book(self, start: int, end: int) -> int:
        self.l.add([start,+1])
        self.l.add([end,-1])
        output = 0
        c = 0
        for i,j in self.l:
            c += j
            output = max(c, output)
        return output
            
        
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)