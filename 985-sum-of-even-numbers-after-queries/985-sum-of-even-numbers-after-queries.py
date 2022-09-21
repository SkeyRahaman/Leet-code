class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ = 0
        output = []
        for i in nums:
            if i%2==0:
                summ += i
        for v,i in queries:
            if v%2==0: #even
                
                if nums[i]%2==0:#even
                    summ += v
                else:
                    pass
            else: # odd
                if nums[i]%2==0:
                    summ -= nums[i]
                else:
                    summ += (v + nums[i])
            nums[i] += v
            # print(nums, summ,v,i)
            output.append(summ)
        return output
                    
                
        