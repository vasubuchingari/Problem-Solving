from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count=Counter(s)
        t_count=Counter(t)
        print(s_count)
        l=[]
        m=[]
        for key,value in s_count.items():
            k=(key,value)
            l.append(k)
        for key,value in t_count.items():
            k=(key,value)
            m.append(k)
        for x in m:
            if x in l:
                pass
            else:
                return x[0]

# OPTIMZED
# from collections import Counter
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         return (Counter(t) - Counter(s)).popitem()[0]


        
