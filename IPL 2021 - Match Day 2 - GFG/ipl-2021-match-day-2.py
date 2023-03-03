#User function Template for python3
from collections import deque
class Solution:
    def max_of_subarrays(self,arr,n,k):
        '''
        you can use collections module here.
        :param a: given array
        :param n: size of array
        :param k: value of k
        :return: A list of required values 
        '''
        #code here
        nums = arr
        mem = deque()
        output = []
        l,r = 0,0
        while r<len(nums):
            while mem and nums[mem[-1]] < nums[r]:
                mem.pop()
            mem.append(r)
            
            if l>mem[0]:
                mem.popleft()
                
            if r+1 >= k:
                output.append(nums[mem[0]])
                l += 1
            r+=1
        return output
        
        output = []
        stack = deque()
        for i,j in enumerate(arr):
            while len(stack) != 0 and arr[stack[-1]] < j:
                stack.pop()
            
            stack.append(i)
            l = max(0,i-k)
            if stack[-1] < (i-k+1):
                stack.popleft()
                
            if i>=k-1:
                output.append(arr[stack[0]])
        return output
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends