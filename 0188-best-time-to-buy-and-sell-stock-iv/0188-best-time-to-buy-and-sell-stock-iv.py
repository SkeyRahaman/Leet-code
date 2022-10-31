class Solution:
    def maxProfit(self, k: int, v: List[int]) -> int:
        n = len(v)
        # dp = [-1,-1] *
        @cache
        def f(i,k,b):
            if i==n or (b and k<=0) :return 0
            
            
            if b:
                return max(-v[i] + f(i+1,k-1,0),f(i+1,k,1))
            else:
                return max( v[i] +f(i+1,k,1),f(i+1,k,0) )
        return f(0,k,1)
            
        