class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digi = []
        lrtt = []
        output = []
        for i in logs:
            x = i.split()
            if x[1].isdigit():
                digi.append(i)
            else:
                lrtt.append(i)
        lrtt.sort(key = lambda x:x.split()[0])
        lrtt.sort(key = lambda x:x.split()[1:])
        return lrtt +digi
                
        