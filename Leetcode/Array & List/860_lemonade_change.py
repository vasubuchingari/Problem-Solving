from collections import Counter
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives=0
        tens=0
        for x in bills:
            if x==5:
                fives+=1
            elif x==10:
                if fives>0:
                    tens+=1
                    fives-=1
                else:
                    return False
            elif x==20:
                if tens>0 and fives>0:
                    tens-=1
                    fives=fives-1
                elif fives>=3:
                    fives-=3
                else:
                    return False
        return True
                

                

                


        
