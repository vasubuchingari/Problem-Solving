class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        count=0
        for x in s:
            if x=="(":
                stack.append(x)
                count=max(count,len(stack))
            elif x==")":
                stack.pop()
        return count
            

        
