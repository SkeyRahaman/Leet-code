class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        res = 0
        num = 0
        stack = []
        for x in s:
            if x.isdigit() :
                num = num*10 + int(x)
            elif x == "+" or x == "-":
                res += sign*num
                num = 0
                sign = [-1,1][x=="+"]
            elif x == "(":
                stack.append([res,sign])
                sign = 1
                res = 0
            elif x == ")":
                res += sign*num
                num = res
                res,sign = stack.pop()
        return res+sign*num
        
        
        