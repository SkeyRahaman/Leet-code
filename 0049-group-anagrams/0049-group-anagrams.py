class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            mem[key].append(i)
        return mem.values()
        