class Solution:
    def maxProfit(self, k: int, v: List[int]) -> int:
        n = len(v)
        @cache
        def f(i,k,b):
            if i==n:return 0
            if b and k>0:
                return max(-v[i] + f(i+1,k-1,0),f(i+1,k,1))
            if not b:
                return max( v[i] +f(i+1,k,1),f(i+1,k,0) )
            else:
                return 0
        return f(0,k,1)
            
        