class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        di={
            ")":"(","]":"[","}":"{"
            }
        for x in s:
            if x in di :
                if  l and l[-1]==di[x]:
                    l.pop()
                else:
                    return False
            else:
                l.append(x)
        return True if not l else False
