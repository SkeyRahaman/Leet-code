from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        c = SortedList()
        output = 0
        for a,b in zip(nums1, nums2):
            output += c.bisect_right(a-b+diff)
            c.add(a-b)
            # print(c,output)
        return output
        