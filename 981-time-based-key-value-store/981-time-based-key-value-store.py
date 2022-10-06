from sortedcontainers import SortedList
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.mem = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mem[key].add([timestamp, value])
        # print(self.mem)
        

    def get(self, key: str, timestamp: int) -> str:
        x = self.mem[key]
        for i in range(len(x)-1,-1,-1):
            if x[i][0] <= timestamp:
                return x[i][1]
        return ""
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)