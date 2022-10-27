class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 10000
        o=0
        for i in prices:
            o = max(i-mx,o)
            mx = min(mx,i)
            # print(mx,i,o)
        return o
        
        