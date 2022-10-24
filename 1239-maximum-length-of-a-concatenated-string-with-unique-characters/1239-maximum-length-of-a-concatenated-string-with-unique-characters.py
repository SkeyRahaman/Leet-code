class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # @cache
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)
    
        def helper(i,have):
            if i == 0:
                notTake = len(have)
                pre = True
                for c in arr[0]:
                    if c in have:
                        pre = False
                        # print(c)
                        break
                    have.add(c)
                # # print(have)
                # if pre:
                #     print("Yes",have)
                take =  len(have) if pre else 0
                return max(take,notTake)
            
            
            notTake = helper(i-1,{z for z in have})
            pre = True
            for c in arr[i]:
                if c in have:
                    pre = False
                    break
                have.add(c)
            take = 0 if not pre else helper(i-1,{z for z in have})
            return max(take,notTake)
        return helper(len(arr)-1,set())
