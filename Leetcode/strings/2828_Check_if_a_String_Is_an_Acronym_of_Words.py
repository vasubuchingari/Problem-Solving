class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        i=0
        if len(words)!=len(s):
            return False
        for x in words:
            if x[0]==s[i]:
                i=i+1
            else:
                return False
        return True
        
