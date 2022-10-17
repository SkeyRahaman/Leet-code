class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len({i for i in sentence}) == 26
        