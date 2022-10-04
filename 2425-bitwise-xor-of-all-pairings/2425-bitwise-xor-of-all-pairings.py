from itertools import chain
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # output = 0
        # if len(nums2) %2 != 0:
        #     for i in nums1:
        #         output ^= i
        #         # print(output)
        # if len(nums1) %2 != 0:
        #     for i in nums2:
        #         output ^= i
        #         # print(output)
        # return output
        # print(reduce(xor, nums2))
        return ((len(nums1) %2) * reduce(xor, nums2)) ^ ((len(nums2) %2) * reduce(xor, nums1))