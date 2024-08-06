class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        res=""
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i]!=strs[-1][i]:
                return res
            else:
                res=res+strs[0][i]    
        return res  


#elements are sorted according to the lexicographically
