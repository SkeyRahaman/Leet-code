class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(n-1):
            o = []
            l = s[0]
            c= 1
            for j in s[1:]:
                if j == l:
                    c+=1
                else:
                    o.append(f"{c}{l}")
                    l = j
                    c = 1
            o.append(f"{c}{l}")
            s = "".join(o)
            # print(s)
        return s
