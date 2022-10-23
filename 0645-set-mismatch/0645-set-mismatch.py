class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)+1
        have = sum(nums)
        need = sum(set(nums))
        d = need - have
        should_have = n*(n-1)//2
        # print(should_have)
        return [have-need,should_have-need]
        