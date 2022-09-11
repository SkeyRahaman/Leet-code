class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store = collections.Counter(s)
        loc = {}
        output = []
        last = 0
        for i,j in enumerate(s):
            if j not in loc:
                if store[j] != 1:
                    loc[j] = store[j] - 1
                else:
                    if len(loc) == 0:
                        output.append(i+1-last)
                        last = i+1
            else:
                if loc[j] == 1:
                    del loc[j]
                    if len(loc) == 0:
                        output.append(i+1-last)
                        last = i+1
                else:
                    loc[j] -= 1
        return output
                
        