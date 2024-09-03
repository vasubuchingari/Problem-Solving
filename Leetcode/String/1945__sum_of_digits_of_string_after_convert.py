class Solution:
    def getLucky(self, s: str, k: int) -> int:
        di = {chr(i): str(i - 96) for i in range(97, 123)}
        
        num=""
        for x in s:
            num=num+di[x]
        i=0
        while i<k:
            tot=0
            for x in num:
                tot=tot+int(x)
            num=str(tot)
            i=i+1

        return tot
