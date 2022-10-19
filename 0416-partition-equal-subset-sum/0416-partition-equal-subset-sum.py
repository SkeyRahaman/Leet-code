class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S%2==1:
            return False
        K = S//2
        
        
        # tabulization will not work because we are checking for all the K which is not required. (MY openion.)
        # mem = [[False] * (K+1) for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     mem[i][0] = True
        # if nums[0]<=K:mem[0][nums[0]] = True
        # for i in range(1,len(nums)):
        #     for j in range(1,K+1):
        #         NT = mem[i-1][j]
        #         TK = False if nums[i] >j else mem[i-1][j-nums[i]]
        #         mem[i][j] = NT or TK
        # return mem[len(nums)-1][K]
                
        
        
        
        
        
        
        
        
        
        # DP SOLUTION
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
        