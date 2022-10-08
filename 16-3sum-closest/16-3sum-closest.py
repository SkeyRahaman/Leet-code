class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:return sum(nums)
        nums.sort()
        output = sum(nums[:3])
        
        
        cur = sum(nums[:3])
        if cur >= target:
            return cur
        
        cur = sum(nums[-3:])
        if cur < target:
            return cur
        
        for i in range(len(nums)-2):
            j,k=i+1,len(nums)-1
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if abs(target-s) < abs(target - output):
                    output = s
                if s<target:
                    j+=1
                elif s> target:
                    k-=1
                else:
                    return s
        return output
        