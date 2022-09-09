class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        p = 0
        for i,j in sorted(Counter(barcodes).items(), key = lambda x :x[1])[::-1]:
            for k in range(j):
                barcodes[p] = i
                p += 2
                if p>=n:
                    p = 1
        return barcodes
        