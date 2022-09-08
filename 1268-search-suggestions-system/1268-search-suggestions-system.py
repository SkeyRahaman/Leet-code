class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        N = len(products)
        products = sorted(products)
        start,end = 0,N-1
        output = []
        for i,j in enumerate(searchWord):
            while(start<=end and (len(products[start]) <= i or j != products[start][i])):
                start += 1
            while(start<=end and (len(products[start]) <= i or j != products[end][i])):
                end -= 1
            if start+2<=end:
                output.append([products[x] for x in range(start,start+3)])
            elif start>end:
                output.append([])
            else:
                output.append([products[x] for x in range(start,end+1)])
            
        return output
                               
            