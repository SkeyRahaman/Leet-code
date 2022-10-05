
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def cmp(a, b):
            return (a > b) - (a < b) 
        a = bin(num1).count("1")
        b = bin(num2).count("1")
        output = num1
        for i in range(32):
            if cmp(a,b) == cmp((1 << i) & num1,0.5):
                output ^= 1 << i
                a -= cmp(a,b)
        return output
        # a, b = bin(num1).count('1'), bin(num2).count('1')
        # res = num1
        # for i in range(32):
        #     if cmp(a, b) == cmp((1 << i) & num1, 0.5):
        #         res ^= 1 << i
        #         a -= cmp(a, b)
        # return res
        