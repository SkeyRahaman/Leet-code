from itertools import chain
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        output = 0
        if len(nums2) %2 != 0:
            for i in nums1:
                output ^= i
                # print(output)
        if len(nums1) %2 != 0:
            for i in nums2:
                output ^= i
                # print(output)
        return output
        # x = y = 0
        # for a in nums1:
        #     x ^= a
        #     print(x)
        # for b in nums2:
        #     y ^= b
        #     print(y)
        # return (len(nums1) % 2 * y) ^ (len(nums2) % 2 * x)