class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        for i in strs:
            mem["".join(sorted(i))].append(i)
        return mem.values()
        