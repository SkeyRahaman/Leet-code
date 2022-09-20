class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2 = len(nums1), len(nums2)
        output = 0
        mem = [[0]*(n1+1) for i in range(n2+1)]
        for i in range(1,n2+1):
            for j in range(1,n1+1):
                if nums1[j-1] == nums2[i-1]:
                    mem[i][j] = 1 + mem[i-1][j-1] 
                    output = max(output,mem[i][j])
        return output
        
        