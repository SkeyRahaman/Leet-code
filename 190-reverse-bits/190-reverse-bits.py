class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            if n & 1 == 1:
                output <<= 1
                output += 1
            else:
                output <<= 1
            n >>= 1
        return output
        