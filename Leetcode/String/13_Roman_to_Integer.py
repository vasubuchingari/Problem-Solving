class Solution:
    def romanToInt(self, s: str) -> int:
        tot=0
        symbol={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range (len(s)):
            if i+1<len(s) and symbol[s[i]]<symbol[s[i+1]]:
                tot=tot-symbol[s[i]]
            else:
                tot=tot+symbol[s[i]]
        return tot
