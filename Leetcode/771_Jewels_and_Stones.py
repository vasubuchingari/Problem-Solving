class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for x in stones:
            if x in jewels:
                count+=1
        return count
        
