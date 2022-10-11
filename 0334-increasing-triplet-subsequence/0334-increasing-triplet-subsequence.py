class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <3:
            return False
        i = float('inf')
        j = float('inf')
        for n in nums:
            if n <= i:
                i = n
            elif n<= j:
                j = n
            else:
                return True
        return False
                
        
        
        
        