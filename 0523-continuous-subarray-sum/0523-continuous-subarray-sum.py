class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen, cur = {0: -1}, 0
        for i, a in enumerate(nums):
            cur = (cur + a) % k
            if i - seen.setdefault(cur, i) > 1: return True
        return False
    
    
        mem = {0:-1}
        s = 0
        for j,i in enumerate(nums):
            s = s+i if k==0 else (s+i)%k
            if s in mem:
                if j-mem[s] >= 2:
                    return True
            mem[s] = i
        return False
                
            
        