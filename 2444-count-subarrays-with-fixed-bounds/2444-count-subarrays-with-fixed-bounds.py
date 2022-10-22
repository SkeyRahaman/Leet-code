class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        output,bad,maxi,mini=0,-1,-1,-1
        for i,n in enumerate(nums):
            if not minK<=n<=maxK:bad = i
            if n==minK:mini=i
            if n==maxK:maxi=i
            output += max(0,min(maxi,mini)-bad)
        return output