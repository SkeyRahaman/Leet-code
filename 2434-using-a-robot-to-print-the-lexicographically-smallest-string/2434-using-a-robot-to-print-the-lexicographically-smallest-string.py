from collections import Counter
class Solution:
    def robotWithString(self, s: str) -> str:
        c = Counter(s)
        output = []
        stack = []
        for i in s:
            stack.append(i)
            if c[i] == 1:
                del c[i]
            else:
                c[i] -= 1
            while c and stack and min(c) >= stack[-1]:
                output.append(stack.pop())
        output += stack[::-1]
        # print(output)
        return "".join(output)