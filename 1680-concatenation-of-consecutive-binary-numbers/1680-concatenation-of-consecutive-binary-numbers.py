class Solution:
    def concatenatedBinary(self, n: int) -> int:
        output = []
        for i in range(1,n+1):
            output.append(bin(i)[2:])
        return int("".join(output),2)%1000000007
        