class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        output = 0
        lastc = "A"
        lastt = 0
        for i,j in zip(colors, neededTime):
            if lastc == i:
                output += min(lastt,j)
                lastt = max(lastt,j)
            else:
                lastc = i
                lastt = j
            # print(lastt,output)
        return output
                    
        