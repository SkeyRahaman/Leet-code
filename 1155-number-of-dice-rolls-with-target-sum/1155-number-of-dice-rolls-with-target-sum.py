class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mem  = [[-1] * target for i in range(n)]
        # print(mem)
        def helper(dice,face,t):
            if t < 0 :
                return 0
            if dice == 0 and t == 0:
                return 1
            if dice == 0 and t != 0:
                return 0
            if dice != 0 and t == 0:
                return 0
            
            
            if mem[dice-1][t-1] != -1:
                return mem[dice-1][t-1]
            
            
            output = 0
            for i in range(1,face+1):
                if t-i <0:
                    break
                output += helper(dice-1,face,t-i)
            mem[dice-1][t-1] = output
            # print(dice,t,output)
            return mem[dice-1][t-1]
        out = helper(n,k,target)
        # print(mem)
        return out%1000000007
        