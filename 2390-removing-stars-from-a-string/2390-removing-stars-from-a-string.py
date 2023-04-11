class Solution:
    def removeStars(self, s: str) -> str:
        output= []
        if "*" not in s:return s
        for i in s:
            if i == "*":
                output.pop()
            else:
                output.append(i)
        return "".join(output)
        
        