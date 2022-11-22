#User function Template for python3
from sortedcontainers import SortedList
class Solution:
	def countTriplets(self, nums):
        output = 0
        for i in range(1,len(nums)-1):
            left = 0
            for l in nums[:i]:
               if l<nums[i]:
                   left += 1
            right = 0
            for r in nums[i+1:]:
               if r>nums[i]:
                   right += 1
            output += (left*right)
        return output
	    
	    
	    
	    
		# Code here
# 		output = 0
# 		for start in range(len(nums)-2):
# 		    l = SortedList()
# 		    for end in range(start+1,len(nums)):
# 		        if nums[start]>=nums[end]:
# 		            continue
# 		        output += l.bisect_left(nums[end])
# 		        l.add(nums[end])
# 		return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int,input().split()))
		ob = Solution()
		ans = ob.countTriplets(nums)
		print(ans)

# } Driver Code Ends