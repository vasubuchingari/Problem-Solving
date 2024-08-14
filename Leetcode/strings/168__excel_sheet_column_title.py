class Solution:
    def convertToTitle(self, num: int) -> str:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        final=""
        while num>0:
            num=num-1
            final=  alpha[num%26]+final
            num=num//26
        
        return final
