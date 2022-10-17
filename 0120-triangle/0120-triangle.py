from functools import lru_cache
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        @lru_cache
        def helper(i,d,h):
            # print(d,h,d ==h)
            if d == h:
                return triangle[d-1][i]
            return triangle[d-1][i] + min(helper(i,d+1,h),helper(i+1,d+1,h))
        return helper(0,1,h)