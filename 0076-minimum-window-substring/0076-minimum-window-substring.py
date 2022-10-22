class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        need_n = len(need)
        have = defaultdict(int)
        have_n = 0
        first = 0
        output = [0,0,float('inf')]
        for i,c in enumerate(s):
            if c in need:
                have[c] += 1
                if have[c] == need[c]:
                    have_n += 1
                if have_n == need_n:
                    for j in range(first,i+1):
                        if s[j] in need:
                            have[s[j]] -= 1
                            if have[s[j]] < need[s[j]]:
                                have_n -= 1
                                break
                        first += 1
                    if output[2] > (i+1)-first:
                        output = [first,i+1,(i+1)-first]
                    first += 1
        # print()
        return s[output[0]:output[1]]
                
        
        