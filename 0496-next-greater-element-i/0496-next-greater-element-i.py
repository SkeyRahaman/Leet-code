class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mem = []
        nums3 = defaultdict(int)
        for i in nums2[::-1]:
            while mem and i > mem[-1]:
                mem.pop()
            if mem:
                nums3[i] = mem[-1] 
            else:
                nums3[i] = -1
            mem.append(i)
        return [nums3[i] for i in nums1]
        