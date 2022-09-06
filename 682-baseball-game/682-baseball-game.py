class Solution:
    def calPoints(self, ops: List[str]) -> int:
        summ = []
        for j,i in enumerate(ops):
            if i.isdigit():
                summ.append(int(i))
            elif i[0] == '-':
                summ.append(-int(i[1:]))
            elif i == '+':
                x = summ[-1] + summ[-2]
                summ.append(x)
            elif i == 'D':
                x = summ[-1]*2
                summ.append(x)
            else:
                summ.pop()
        return sum(summ)