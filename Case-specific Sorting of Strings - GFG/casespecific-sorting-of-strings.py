#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        l = [i for i in s if i.islower()]
        l.sort(reverse = True)
        u = [i for i in s if i.isupper()]
        u.sort(reverse = True)
        # print(l,u)
        # print('a'.islower())
        output = []
        for i in s:
            if i.islower():
                output.append(l.pop())
            else:
                output.append(u.pop())
        return "".join(output)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends