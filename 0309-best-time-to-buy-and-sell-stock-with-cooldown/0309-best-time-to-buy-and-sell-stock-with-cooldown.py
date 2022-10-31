class Solution:
    def maxProfit(self, v: List[int]) -> int:
        n = len(v)
        @cache
        def f(i,b,c):
            if i == n:
                return 0
            if c == 0:
                if b:
                    return max(-v[i] + f(i+1,0,0), f(i+1,1,0))
                else:
                    return max(v[i] + f(i+1,1,1), f(i+1,0,0))
            else:
                return f(i+1,b,c-1)
        return f(0,1,0)
        