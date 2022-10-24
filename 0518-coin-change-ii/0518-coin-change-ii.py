class Solution:
    def change(self, amount: int, nums: List[int]) -> int:
        @cache
        def helper(i,t):
            if i == 0:
                if t%nums[0]==0:
                    return 1
                else:
                    return 0
            notTake = helper(i-1,t)
            take = 0
            if nums[i] <= t:
                take = helper(i,t-nums[i])
            return take + notTake
        return helper(len(nums)-1,amount)
            