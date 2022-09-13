class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = sorted(Counter(words).items(), key=lambda x:x[0])
        words = sorted(words, key=lambda x:-x[1])
        return [s[0] for s in words[:k]]
        
        