class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = [float('inf'), 0, 0] # length , start , end
        need = Counter(t)
        have = dict()
        have_n = 0
        first = 0
        need_n = len(need)
        for i,c in enumerate(s):
            if c in need:
                # print(c)
                if c in have:
                    have[c] += 1
                else:
                    have[c] = 1
                if need[c] == have[c]:
                    have_n += 1
                if have_n == need_n:
                    pp = first
                    for k in range(pp,i+1):
                        # print(output,c,have,need,have_n,first,i)
                        if s[k] in need:
                            have[s[k]] -= 1
                            if need[s[k]] > have[s[k]]:
                                have_n -= 1
                                break
                            else:
                                first += 1
                        else:
                            first += 1   
                    length = i-first+1
                    if length < output[0]:
                        output = [length,first,i+1]
                    first += 1
        return s[output[1]:output[2]]