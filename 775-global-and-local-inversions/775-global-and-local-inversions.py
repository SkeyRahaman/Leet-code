class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i,j in enumerate(nums):
            if not abs(i-j) <= 1:
                return False
        return True
            