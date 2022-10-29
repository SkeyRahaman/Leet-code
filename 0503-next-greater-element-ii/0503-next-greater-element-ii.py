class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mem = []
        output = []
        N = len(nums)
        for i in range((N*2)-1,-1,-1):
            while mem and nums[i%N] >= mem[-1]:
                mem.pop()
            if mem:
                output.append(mem[-1])
            else:
                output.append(-1)
            mem.append(nums[i%N])
        return output[N:][::-1]