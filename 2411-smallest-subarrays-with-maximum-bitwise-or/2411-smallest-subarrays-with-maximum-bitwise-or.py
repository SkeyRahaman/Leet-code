class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        last = [0] * 32
        N = len(nums)
        output = [0] * N
        
        for i in range(N-1,-1,-1):
            for j in range(32):
                if nums[i] & (1<<j):
                    last[j] = i
            output[i] = max(1,max(last) - i + 1)
        
        return output
        
        