class Solution:
    def maxProfit(self, k: int, v: List[int]) -> int:
        n = len(v)
        @cache
        def f(i,b,k):
            if i==n:return 0
            if b and k>0:
                return max(-v[i] + f(i+1,0,k-1),f(i+1,1,k))
            if not b:
                return max( v[i] +f(i+1,1,k),f(i+1,0,k) )
            else:
                return 0
        return f(0,1,k)
            
        