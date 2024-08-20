class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(n):
            tot=0
            while n>0:
                curr=n%10
                tot=tot+curr*curr
                n=n//10
            return tot
        seen_num=set()
        while n!=1 and n not in seen_num:
            seen_num.add(n)
            k=next_num(n)
            n=k

        return n==1
