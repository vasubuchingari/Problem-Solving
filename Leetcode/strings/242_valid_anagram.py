class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=list(s)
        l2=list(t)
        s1=sorted(l1)
        s2=sorted(l2)
        if s1!=s2:
            return False
        return True      
