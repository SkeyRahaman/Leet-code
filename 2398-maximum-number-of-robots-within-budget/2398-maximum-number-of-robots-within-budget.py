class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        N = len(chargeTimes)
        mem = collections.deque()
        l,r =0,0
        run_sum = 0
        output = 0
        while r<N:
            run_sum += runningCosts[r]
            while mem and chargeTimes[mem[-1]] < chargeTimes[r]:
                mem.pop()
            mem.append(r)
            # print(mem)
            cost= (r-l+1)*run_sum + chargeTimes[mem[0]]
            if cost <= budget :
                output = max(output,r-l+1)
            else:
                while cost >= budget:
                    if mem[0] == l:
                        mem.popleft()
                    run_sum -= runningCosts[l]
                    l += 1
                    if mem:
                        cost = (r-l+1)*run_sum + chargeTimes[mem[0]] 
                    else:
                        cost = 0
            
            r += 1
        return output
            
        