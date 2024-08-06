from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count=Counter(arr)
        distinct_count=0
        for x in arr:
            if count[x]==1:
                distinct_count+=1
                if distinct_count==k:
                    return x
        return ""


# from collections import Counter

# class Solution:
#     def kthDistinct(self, arr: List[str], k: int) -> str:
#         count=Counter(arr)
#         li=[]
#         for x in arr:
#             if count[x]==1:
#                 li.append(x)
                
#         print(li)

#         if k-1 < len(li):
#             return li[k-1]
#         else:
#             return ""
                
    
        
