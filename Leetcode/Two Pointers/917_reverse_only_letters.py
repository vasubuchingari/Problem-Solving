class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        while left<right:
            while left<right and not s[left].isalpha():
                left=left+1
            while left<right and not s[right].isalpha():
                right=right-1
            s[left],s[right]=s[right],s[left]
            left=left+1
            right=right-1

        return "".join(s)
