class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        earn = []
        loss = []
        for a,b in transactions:
            if a-b>=0:
                loss.append([a,b])
            elif a-b<0:
                earn.append([a,b])
        earn.sort(key=lambda x:x[0], reverse=True)
        loss.sort(key=lambda x:x[1], reverse=False)
        output = 0
        cost = 0
        for a,b in chain(loss,earn):
            cost += a
            output = max(output,cost)
            cost-=b
        return output
            
            
                