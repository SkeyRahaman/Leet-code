class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # return len(set(sentence)) == 26
        a = set()
        for i in sentence:
            a.add(i)
            if len(a) == 26:
                return True
        return False
        