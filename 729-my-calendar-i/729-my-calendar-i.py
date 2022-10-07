from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.mem = SortedList()

    def book(self, start: int, end: int) -> bool:
        u = self.mem.bisect_right([start,end])
        # print(u)
        if 0<=u-1<len(self.mem):
            if start < self.mem[u-1][1] :
                return False
        if 0<=u<len(self.mem):
            if self.mem[u][0] < end:
                return False
            
        self.mem.add([start,end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)