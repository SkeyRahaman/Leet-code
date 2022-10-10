class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i,j in enumerate(palindrome):
            for c in string.ascii_lowercase:
                if c == j:
                    break
                x = palindrome[:i] + 'a' + palindrome[i+1:]
                if x != x[::-1]:
                    return x
        # for i in range(len(palindrome)-1,-1,-1):
        #     if palindrome[i] 
        return palindrome[:-1] + 'b'
        