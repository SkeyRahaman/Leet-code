class Solution:
    def maxProfit(self, v: List[int], fee: int) -> int:
        n = len(v)
        last = [0,0]
        cur = [0,0] 
        for i in range(n-1,-1,-1):
            cur[0] = max(v[i] + last[1], last[0])
            cur[1] = max(-v[i] + last[0] - fee, last[1])
            last = [cur[0],cur[1]]
        return last[1]