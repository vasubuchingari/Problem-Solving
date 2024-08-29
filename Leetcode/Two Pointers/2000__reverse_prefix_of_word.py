class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        p1 = 0
        rev = ""
        found = False
        for i in range(len(word)):
            if word[i] == ch:
                rev = word[p1:i+1]
                rev = rev[::-1]
                found = True
                break
        
        if found:
            left = word[i+1:]
            return rev + left
        else:
            return word  
