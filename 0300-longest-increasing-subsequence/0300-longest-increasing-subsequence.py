from sortedcontainers import SortedList
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = SortedList()
        for i in nums:
            add = mem.bisect_left(i)
            # if add > 0 and mem[add-1] == i:
            #     add -= 1
            if add != len(mem):
                mem.discard(mem[add])
            mem.add(i)
        return len(mem)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        n = len(nums)
        last = [0 for i in range(n+1)]
        cur = [0 for i in range(n+1)]
        for ind in range(n-1,-1,-1):
            for pre in range(-1,ind,1):
                notTake = last[pre]
                take = 0
                if (pre == -1) or nums[ind] > nums[pre]:
                    take = 1 + last[ind]
                cur[pre] =  max(notTake,take)
            last = [z for z in cur]
            cur = [0 for i in range(n+1)]
        return last[-1]

        
        
        
        
        
        n = len(nums)
        dp = [[-1 for i in range(n+1)] for _ in range(n+1)]
        def f(ind,pre):
            if ind == n:
                return 0
            if dp[ind][pre] != -1:
                return dp[ind][pre]
            
            
            
            notTake = f(ind+1,pre)
            take = 0
            if (pre == -1) or nums[ind] > nums[pre]:
                take = 1 + f(ind+1,ind)
            dp[ind][pre] =  max(notTake,take)
            return dp[ind][pre]
        return f(0,-1)
        