class Solution:
    def equalFrequency(self, word: str) -> bool:
        # for i in range(len(word)):
        #     x= word[:i] + word[i+1:]
        #     c = Counter(word[:i] + word[i+1:])
        #     v = Counter(word[:i] + word[i+1:]).values()
        #     print(len(set(Counter(word[:i] + word[i+1:]).values())) == 1)
        return any([len(set(Counter(word[:i] + word[i+1:]).values())) == 1 for i in range(len(word))])
            