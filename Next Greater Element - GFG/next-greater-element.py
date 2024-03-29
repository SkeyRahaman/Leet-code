#User function Template for python3

from collections import deque
import bisect
class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        output = []
        stack = deque([float('inf')])
        for i in arr[::-1]:
            n = bisect.bisect_right(stack,i)
            output.append(-1 if stack[n] == float('inf') else stack[n])
            while stack[0] <= i:
                stack.popleft()
            stack.appendleft(i)
        return output[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

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
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends