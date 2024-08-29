class Solution: 

    def mergeAlternately(self, word1: str, word2: str) -> str: 
        i,j=0,0 
        l=[]
        while i<len(word1) and j<len(word2): 
            l.append(word1[i])
            l.append(word2[j])
            i=i+1
            j=j+1
        l.append(word1[i:])
        l.append(word2[j:])
        return "".join(l)
            

