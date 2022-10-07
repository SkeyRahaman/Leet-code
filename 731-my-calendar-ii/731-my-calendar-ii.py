from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.mem = SortedList()
        

    def book(self, start: int, end: int) -> bool:
        self.mem.add([start,1])
        self.mem.add([end, -1])
        c = 0
        for _, b in self.mem:
            c+=b
            if c > 2:
                self.mem.remove([start,1])
                self.mem.remove([end, -1])
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)