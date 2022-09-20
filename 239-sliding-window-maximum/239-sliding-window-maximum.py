class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mem = collections.deque()
        output = []
        l,r = 0,0
        while r<len(nums):
            while mem and nums[mem[-1]] < nums[r]:
                mem.pop()
            mem.append(r)
            
            if l>mem[0]:
                mem.popleft()
                
            if r+1 >= k:
                output.append(nums[mem[0]])
                l += 1
            r+=1
        return output
        
        
