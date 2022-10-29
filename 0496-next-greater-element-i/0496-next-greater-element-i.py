class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mem = []
        nums3 = defaultdict(int)
        for i in range(len(nums2)-1,-1,-1):
            while mem and nums2[i] > mem[-1]:
                mem.pop()
            if mem:
                nums3[nums2[i]] = mem[-1] 
            else:
                nums3[nums2[i]] = -1
            mem.append(nums2[i])
        return [nums3[i] for i in nums1]
        