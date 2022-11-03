class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        output = 0
        mem = defaultdict(int)
        for i in words:
            if i in mem:
                mem[i] -= 1
                if mem[i] == 0:
                    del mem[i]
                output += 4
                # print(i)
            else:
                mem[i[::-1]] += 1
        for a,b in mem:
            if a==b:
                # print(a,b)
                return output + 2
        else:
            return output