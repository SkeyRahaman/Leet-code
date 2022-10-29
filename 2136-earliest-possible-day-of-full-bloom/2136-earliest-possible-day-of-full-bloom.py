class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        data = [[i,j] for i,j in zip(plantTime, growTime)]
        data.sort(reverse=True,key=lambda x:x[1])
        # print(data)
        output = 0
        start=0
        for i,j in data:
            start += i
            output = max(output,start+j)
        return output
        