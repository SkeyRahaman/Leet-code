class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <3:
            return max(nums)
        n1 = nums[0]
        n2 = max(nums[:2])
        for i in nums[2:]:
            x = max(n2,i+n1)
            n1 = n2
            n2 = x
        return n2
        