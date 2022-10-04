class LUPrefix:

    def __init__(self, n: int):
        self.mem = [False] * (n+1)
        self.count = -1
        self.cap = n
    def arrange(self):
        while self.count < self.cap and self.mem[self.count+1] == True:
            # print(self.count)
            self.count += 1
            
        

    def upload(self, video: int) -> None:
        self.mem[video-1] = True
        self.arrange()
        

    def longest(self) -> int:
        return self.count+1
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()