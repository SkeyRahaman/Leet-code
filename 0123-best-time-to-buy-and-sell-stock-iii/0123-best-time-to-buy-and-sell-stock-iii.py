class Solution:
    def maxProfit(self, v: List[int]) -> int:
        n = len(v)
        @cache
        def f(i,b,t):
            if i == n:return 0
            if b and t == 0:return 0
            if b:
                return max(-v[i] + f(i+1,0,t-1),  f(i+1,1,t))
            else:
                return max(+v[i] + f(i+1,1,t), f(i+1,0,t))
        return f(0,1,2)
        
        
        
        