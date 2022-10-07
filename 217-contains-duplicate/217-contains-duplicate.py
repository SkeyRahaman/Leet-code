class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = set()
        for i in nums:
            if i in mem:
                return True
            mem.add(i)
        return False
        