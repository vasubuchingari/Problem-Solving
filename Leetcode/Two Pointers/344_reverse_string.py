class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length=len(s)
        i,j=0,length-1
        for i in range(length//2):
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            j=j-1
            i=i+1
        
