class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        output = ""
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/{nums[1]}"
        return f"{nums[0]}/({'/'.join([str(x) for x in nums[1:]])})"
        
        