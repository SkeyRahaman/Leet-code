class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache
        def helper(i,j):
            if i==0 and j == 0:
                return 1
            if i<0 or j <0:
                return 0
            top = helper(i-1,j)
            left = helper(i,j-1)
            return top+left
        return helper(m-1,n-1)