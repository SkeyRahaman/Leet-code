from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.score = SortedList()
        self.count = -1
        

    def add(self, name: str, score: int) -> None:
        self.score.add((-score,name))
        
        

    def get(self) -> str:
        self.count+=1
        return self.score[self.count][1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()