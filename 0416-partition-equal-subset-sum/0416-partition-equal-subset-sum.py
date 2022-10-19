class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S%2==1:
            return False
        K = S//2
        mem = [[-1] * (K+1) for _ in range(len(nums))]
        def helper(i,k):
            if mem[i][k] != -1:return mem[i][k]
            if k == 0:return True
            if i == 0 : return nums[0] == k
            not_take = helper(i-1,k)
            take = False
            if nums[i] <= k : take = helper(i-1,k-nums[i])
            mem[i][k] =  take or not_take
            return mem[i][k]
        return helper(len(nums)-1,K)
        