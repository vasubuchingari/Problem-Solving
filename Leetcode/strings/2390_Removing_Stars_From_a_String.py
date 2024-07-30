class Solution:
    def removeStars(self, s: str) -> str:
        l=[]
        for i in range(len(s)):
            if s[i]=='*':
                l.pop()
            else:
                l.append(s[i])
        return "".join(l)
