class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mem = {}
        for j,i in enumerate(nums):
            if i in mem:
                if j-mem[i] <= k:
                    return True
            mem[i] = j
        return False
        