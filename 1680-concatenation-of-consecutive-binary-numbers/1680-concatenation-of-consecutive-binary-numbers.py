class Solution:
    def concatenatedBinary(self, n: int) -> int:
        output = 0
        for i in range(1,n+1):
            output = (output << i.bit_length() | i)%1000000007
        return output
        