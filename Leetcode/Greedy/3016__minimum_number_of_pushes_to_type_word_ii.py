from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq=Counter(word)
        print(freq)
        print(freq.items())
        sorted_chars=sorted(freq.items(),key=lambda x: -x[1])
        print(sorted_chars)
        tot=0
        for i,(char,count) in enumerate(sorted_chars):
            #no of presses count if it exceeds 8 two times
            presses=i//8+1
            tot=tot+presses*count

        return tot
